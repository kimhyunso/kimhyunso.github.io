---
title:  "스프링 부트 시작하기"
layout: single
categories:
    - spring
tags:
    - 스프링 부트
---

# 스프링 부트 시작
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

# 스프링 컨테이너

# 의존성 주입 (DI: Depandency Injection)
## `@Autowired`
1. 필드
2. 생성자 : 권장
3. setter
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
repository 및 service

## View
페이지를 보여주는 공간 (html, json 등)

## Controller
API 호출하여 비지니스 로직을 처리할 수 있게 도와주는 역활 및 라우터 역활


## `@RestController`
RestAPI를 사용할 수 있도록 도와주는 어노테이션

`@Controller`와의 차이점 : `@Controller` 어노테이션은 라우터 역활을 하는 방면, `@RestContoller` 어노테이션은 JSON 형태로 데이터를 반환함

## `@Gett`
```java
@RequestMapping("/api")
@RestController
@RequiredArgsConstructor
public class RestAPIController{
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






