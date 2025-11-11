import sys
from typing import Optional, Tuple
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor
import struct
import time

@dataclass
class Complex:
    re: float
    im: float

    def __mul__(self, other: 'Complex') -> 'Complex':
        return Complex(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re
        )

    def __add__(self, other: 'Complex') -> 'Complex':
        return Complex(self.re + other.re, self.im + other.im)

    def norm_sqr(self) -> float:
        return self.re * self.re + self.im * self.im


def escape_time(c: Complex, limit: int) -> Optional[int]:
    z = Complex(0.0, 0.0)
    for i in range(limit):
        if z.norm_sqr() > 4.0:
            return i
        z = z * z + c
    return None


def parse_pair(s: str, separator: str) -> Optional[Tuple[float, float]]:
    try:
        idx = s.find(separator)
        if idx == -1:
            return None
        left = float(s[:idx])
        right = float(s[idx + 1:])
        return (left, right)
    except ValueError:
        return None


def parse_complex(s: str) -> Optional[Complex]:
    result = parse_pair(s, ',')
    if result is None:
        return None
    re, im = result
    return Complex(re, im)


def pixel_to_point(
        bounds: Tuple[int, int],
        pixel: Tuple[int, int],
        upper_left: Complex,
        lower_right: Complex
) -> Complex:
    width = lower_right.re - upper_left.re
    height = upper_left.im - lower_right.im

    return Complex(
        upper_left.re + pixel[0] * width / bounds[0],
        upper_left.im - pixel[1] * height / bounds[1]
    )


def render(
        pixels: list,
        bounds: Tuple[int, int],
        upper_left: Complex,
        lower_right: Complex
):
    assert len(pixels) == bounds[0] * bounds[1]

    for row in range(bounds[1]):
        for column in range(bounds[0]):
            point = pixel_to_point(bounds, (column, row), upper_left, lower_right)
            count = escape_time(point, 255)

            if count is None:
                pixels[row * bounds[0] + column] = 0
            else:
                pixels[row * bounds[0] + column] = 255 - count


def render_band(args):
    band, band_bounds, band_upper_left, band_lower_right, top = args
    render(band, band_bounds, band_upper_left, band_lower_right)
    return band, top


def write_image(filename: str, pixels: list, bounds: Tuple[int, int]):
    width, height = bounds

    # PNG 파일 생성 (간단한 구현)
    with open(filename, 'wb') as f:
        # PNG signature
        f.write(b'\x89PNG\r\n\x1a\n')

        # IHDR chunk
        ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 0, 0, 0, 0)
        write_chunk(f, b'IHDR', ihdr_data)

        # IDAT chunk
        import zlib
        raw_data = b''
        for y in range(height):
            raw_data += b'\x00'  # filter type
            raw_data += bytes(pixels[y * width:(y + 1) * width])

        compressed = zlib.compress(raw_data, 9)
        write_chunk(f, b'IDAT', compressed)

        # IEND chunk
        write_chunk(f, b'IEND', b'')


def write_chunk(f, chunk_type: bytes, data: bytes):
    import struct
    import binascii

    length = len(data)
    f.write(struct.pack('>I', length))
    f.write(chunk_type)
    f.write(data)
    crc = binascii.crc32(chunk_type + data) & 0xffffffff
    f.write(struct.pack('>I', crc))


def main():
    args = sys.argv

    if len(args) != 5:
        print(f"Usage: {args[0]} FILE PIXELS UPPERLEFT LOWERRIGHT", file=sys.stderr)
        print(f"Example: {args[0]} mandel.png 1000x650 -1.20,0.35 -1,0.20", file=sys.stderr)
        sys.exit(1)

    # Parse arguments
    bounds_result = parse_pair(args[2], 'x')
    if bounds_result is None:
        print("error parsing image dimensions", file=sys.stderr)
        sys.exit(1)
    bounds = (int(bounds_result[0]), int(bounds_result[1]))

    upper_left = parse_complex(args[3])
    if upper_left is None:
        print("error parsing upper left", file=sys.stderr)
        sys.exit(1)

    lower_right = parse_complex(args[4])
    if lower_right is None:
        print("error parsing lower right", file=sys.stderr)
        sys.exit(1)

    # Create pixel buffer
    pixels = [0] * (bounds[0] * bounds[1])

    # Parallel rendering
    threads = 8
    rows_per_band = bounds[1] // threads + 1

    tasks = []
    for i in range(threads):
        top = rows_per_band * i
        if top >= bounds[1]:
            break

        height = min(rows_per_band, bounds[1] - top)
        band_size = height * bounds[0]
        band = [0] * band_size

        band_bounds = (bounds[0], height)
        band_upper_left = pixel_to_point(bounds, (0, top), upper_left, lower_right)
        band_lower_right = pixel_to_point(bounds, (bounds[0], top + height), upper_left, lower_right)

        tasks.append((band, band_bounds, band_upper_left, band_lower_right, top))

    # Execute in parallel
    with ThreadPoolExecutor(max_workers=threads) as executor:
        results = executor.map(render_band, tasks)

        # Merge results
        for band, top in results:
            start_idx = top * bounds[0]
            for i, pixel_value in enumerate(band):
                pixels[start_idx + i] = pixel_value

    # Write output
    try:
        write_image(args[1], pixels, bounds)
    except Exception as e:
        print(f"error writing png file: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    start_time = time.time()
    print(f"Starting execution at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")

    main()

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"\nExecution completed at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
    print(f"Total elapsed time: {elapsed_time:.4f} seconds")
    print(f"Total elapsed time: {elapsed_time * 1000:.2f} milliseconds")