import sys
from concurrent.futures import ProcessPoolExecutor
import struct
import time
import zlib
import binascii
from numba import njit

@njit(fastmath=True)
def escape_time(re_c, im_c, limit):
    re_z = 0.0
    im_z = 0.0
    for i in range(limit):
        # z = z*z + c
        re2 = re_z * re_z - im_z * im_z + re_c
        im2 = 2.0 * re_z * im_z + im_c
        re_z, im_z = re2, im2

        if re_z * re_z + im_z * im_z > 4.0:
            return i
    return None

@njit(fastmath=True)
def pixel_to_point(width, height, x, y, ul_re, ul_im, lr_re, lr_im):
    return (
        ul_re + x * (lr_re - ul_re) / width,
        ul_im - y * (ul_im - lr_im) / height
    )

@njit(fastmath=True)
def render_band(args):
    (width, height, ul_re, ul_im, lr_re, lr_im, y_start, y_end) = args
    band = []

    for y in range(y_start, y_end):
        for x in range(width):
            re, im = pixel_to_point(width, height, x, y, ul_re, ul_im, lr_re, lr_im)
            count = escape_time(re, im, 255)
            band.append(0 if count is None else 255 - count)

    return y_start, band


def write_chunk(f, chunk_type, data):
    f.write(struct.pack(">I", len(data)))
    f.write(chunk_type)
    f.write(data)
    crc = binascii.crc32(chunk_type + data) & 0xffffffff
    f.write(struct.pack(">I", crc))


def write_image(filename, pixels, width, height):
    with open(filename, "wb") as f:
        f.write(b'\x89PNG\r\n\x1a\n')
        ihdr = struct.pack(">IIBBBBB", width, height, 8, 0, 0, 0, 0)
        write_chunk(f, b'IHDR', ihdr)

        raw = bytearray()
        for y in range(height):
            raw.append(0)
            raw.extend(pixels[y * width:(y + 1) * width])

        write_chunk(f, b'IDAT', zlib.compress(raw, 9))
        write_chunk(f, b'IEND', b'')


def main():
    file = sys.argv[1]
    w, h = map(int, sys.argv[2].split('x'))
    ul_re, ul_im = map(float, sys.argv[3].split(','))
    lr_re, lr_im = map(float, sys.argv[4].split(','))

    pixels = [0] * (w * h)
    workers = 8
    rows_per = h // workers + 1

    args = []
    for i in range(workers):
        y_start = rows_per * i
        y_end = min(h, y_start + rows_per)
        if y_start >= h:
            break
        args.append((w, h, ul_re, ul_im, lr_re, lr_im, y_start, y_end))

    with ProcessPoolExecutor(workers) as pool:
        for y_start, band in pool.map(render_band, args):
            pixels[y_start * w:y_start * w + len(band)] = band

    write_image(file, pixels, w, h)


if __name__ == "__main__":
    start = time.time()
    main()
    print(f"Time: {time.time() - start:.3f}s")
