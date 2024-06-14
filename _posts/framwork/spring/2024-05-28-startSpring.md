---
title:  "스프링 부트 시작하기"
layout: single
categories:
    - spring
tags:
    - 스프링 부트
---

## 스프링 부트 시작
> **https://start.spring.io**

## Dependencies
필요 라이브러리 추가

### Group
> 도메인 명
>
> 예시 : naver.com
> 
> Groupid : com.naver
>
> 하위 Groupid : com.naver.map
>
> 하위 Groupid : com.naver.web

### Artifact
> 프로젝트의 이름 사용
>
> 이 이름으로 컴파일된  Jar 생성
>
> 소문자로만 작성/특수문자 사용 금지

### Name
> 물리적으로 생성되는 프로젝트명
>
> Artifact와 비슷하여 같은 이름을 쓰는 경우가 많음

## 스프링 컨테이너

## 의존성 주입 (DI: Depandency Injection)
## `@Autowired`
> 필드
>
> 생성자 : 권장
> 
> setter

```java
@Controller
public class Controller{
    @Autowired
    private Service service1; // 필드 의존성 주입
    private Service service2;
    private Service service3;

    @Autowired
    public Contoller(Service service2){ // 생성자 의존성 주입 : 권장
        this.service2 = service2;
    }

    @Autowired
    public Service setService3(Service service3){ // setter 의존성 주입        
        this.service3 = service3;
    }
}
```
## `@RequiredArgsConstructor`
> 생성자 의존성 주입을 하기 위해 사용하는 어노테이션

```java
@Controller
@RequiredArgsConstructor
public class Controller{
    private final Service service; // 의존성 주입
}
```

# MVC 패턴
디자인 패턴 중 하나
- M : Model
- V : View
- C : Controller
## Model
데이터를 저장하는 공간

## View
페이지를 보여주는 공간 (html, json 등)

## Controller
API 호출하여 비지니스 로직을 처리할 수 있게 도와주는 역활 및 라우터 역활


## `@RestController`
RestAPI를 사용할 수 있도록 도와주는 어노테이션

`@Controller`와의 차이점 : `@Controller` 어노테이션은 라우터 역활을 하는 방면, `@RestContoller` 어노테이션은 JSON 형태로 데이터를 반환함

## `@GetMapping`, `@PostMapping`, `@PutMapping`, `@DeleteMapping`
GET, POST, PUT, DELETE

## `@RequestBody`
PUT, POST 는 header와 body부분으로 분리되어 데이터를 전달하기 때문에

요청한 body 부분을 받아올 수 있음

![스크린샷 2024-05-31 오전 9 00 35](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/ce7d2768-8bbf-4bdb-983b-aa103b48b5d6)
{: .align-center}

## `@ResponseEntity`
요청한 내용을 비지니스 로직을 통해 가공 후 객체로 반환해주는 작업


![스크린샷 2024-05-31 오전 9 32 22](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/2b4c70a2-b675-4da3-a9f2-278e6a9ffb14)
{: .align-center}

### `@RestController`
```java
@RequestMapping("/api")
@RestController
@RequiredArgsConstructor
public class BlogAPIController{

    private final BlogService blogService;

    @GetMapping(values = "/articles/{id}")
    public ResponseEntity<ArticleResponse> findByIdArticle(@PathVariable Long id){
        Article article = blogService.findById(id);

        return  ResponseEntity.ok()
                .body(new ArticleResponse(article));
    }

    @PostMapping("/articles")
    public ResponseEntity<Article> addArticle(@RequestBody AddArticleRequest request){
        Article savedArticle = blogService.save(request);

        return ResponseEntity.status(HttpStatus.CREATED)
                .body(savedArticle);
    }

    @DeleteMapping("/articles/{id}")
    public ResponseEntity<Void> deleteArticle(@PathVariable Long id){
        blogService.delete(id);

        return ResponseEntity.ok()
                .build();
    }

    @PutMapping("/articles/{id}")
    public ResponseEntity<Article> updateArticle(@PathVariable Long id, @RequestBody UpdateArticleRequest request){
        Article updateArticle = blogService.update(id, request);

        return ResponseEntity.ok()
                .body(updateArticle);
    }

    @GetMapping("/articles")
    public ResponseEntity<List<ArticleResponse>> findAllArticles(){
        List<ArticleResponse> articles = blogService.findAll()
                .stream()
                .map(ArticleResponse::new)
                .toList();

        return ResponseEntity.ok()
                .body(articles);
    }
}
```
### `@Controller`
라우터 역활을 한다.

`Model` : html에 데이터를 전달해주기 위한 객체

`String`으로 리턴시, 물리적 위치에서 해당 파일을 찾아 보여준다. -> 뷰리졸버와 연관이 있다.

```java
@RequiredArgsConstructor
@Controller
public class BlogViewController {

    private final BlogService blogService;

    @GetMapping("/articles")
    public String getArticles(Model model){
        List<ArticleListViewResponse> articles = blogService.findAll()
                .stream()
                .map(ArticleListViewResponse::new)
                .toList();
        model.addAttribute("articles", articles);

        return "articleList";
    }

    @GetMapping("/articles/{id}")
    public String getArticle(@PathVariable Long id, Model model){
        Article article = blogService.findById(id);
        model.addAttribute("article", article);

        return "article";
    }
    // ...
}
```

## 뷰리졸버
> prefix : 물리적 위치
>
> suffix : 파일 확장자명

```properties
spring.mvc.view.prefix=/WEB-INF/views/
spring.mvc.view.suffix=.jsp
```

## 동작형태
![스크린샷 2024-05-31 오전 9 38 48](https://github.com/kimhyunso/kimhyunso.github.io/assets/87798982/08570318-1f8f-4a81-a724-e91dc36dec84)
{: .align-center}




