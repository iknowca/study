# ParameterizedTypeReference<T>

ParameterizedTypeReference<T>는 스프링에서 제네릭 타입 정보를 런타임에 유지하기 위해서 사용되는 클래스이다.
주로 RestTemplate나 WebClient와 같은 HTTP 클라이언트에서 사용된다.

## 사용 이유
자바에서는 제네릭 타입 정보가 컴파일 타임에만 존재하고, 런타임에는 지워지는 문제가 발생한다(type erasure).
그래서 RestTemplate등에서는 기본적인 방식으로는 제네릭 정보를 유지할 수 없다.

```java
RestTemplate restTemplate = new RestTemplate();
ResponseEntity<List<MyObject>> response =
    restTemplate.exchange("http://example.com/api", HttpMethod.GET, null, new TypeReference<List<MyObject>>() {});

List<MyObject> body = response.getBody();
```

위 코드에서는 ResponseEntity<List<MyObject>>의 타입정보가 런타임에 사라지기 때문에 에러가 발생한다.

## ParameterizedTypeReference<T>
```java
RestTemplate restTemplate = new RestTemplate();

ResponseEntity<List<MyObject>> response = restTemplate.exchange(
    "http://example.com/api",
    HttpMethod.GET,
    null,
    new ParameterizedTypeReference<List<MyObject>>() {}
);

List<MyObject> body = response.getBody();
```

`new ParameterizedTypeReference<List<MyObject>>() {}`처럼 익명 클래스를 사용하면, 제네릭 타입 정보가 런타임까지 유지된다.