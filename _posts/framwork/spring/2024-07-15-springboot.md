---
title:  "스프링 부트 - CRUD"
layout: single
categories:
    - spring
tags:
    - 스프링 부트
---

## 구조
```
|-main
|   |-src
|      L com
|         L example
|             L domain
|                 L Article.java
|             L dto
|                 L RequestArticle.java
|                 L ResponseArticle.java
|             L controller
|                 L AppController.java
|             L service
|                 L AppService.java
|             L repository
|                 L AppRepository.java
|             L Application.java
```
## CRUD
```java
@RestController
@RequiredArgsConstructor
@RequestMapping("/api")
public class ArticleController {
    private final ArticleService articleService;

    @GetMapping("/articles")
    public ResponseEntity<List<ResponseArticle>> findAllArticles() {
        List<ResponseArticle> articles = articleService.selectAll()
                                        .stream()
                                        .map(ResponseArticle::new)
                                        .toList();

        return ResponseEntity.status(HttpStatus.OK)
                    .body(articles);
    }

    @GetMapping("/article/{id}")
    public ResponseEntity<ResponseArticle> findByIdArticle(@PathVariable("id") Long id) {

        return ResponseEntity.status(HttpStatus.OK)
                    .body(new ResponseArticle(articleService.selectById(id)));
    }


    @PutMapping("/article/{id}")
    public ResponseEntity<Article> updateArticle(@PathVariable("id") Long id, @RequestBody RequestArticle article) {
        Article updateArticle = articleService.update(article, id);

        return ResponseEntity.status(HttpStatus.OK)
                    .body(article);
    }

    @PostMapping("/article")
    public ResponseEntity<Article> saveArticle(@RequestBody RequestArticle article) {
        Article saveArticle = articleService.insert(article);

        return ResponseEntity.status(HttpStatus.CREATED)
                    .body(article);
    }

    @DeleteMapping("/article/{id}")
    public ResponseEntity<Void> deleteArticle(@PathVariable("id") Long id) {
        articleService.deleteById(id);

        return ResponseEntity.ok()
                .build();
    }
}

@Service
@RequiredArgsConstructor
public class ArticleService {
    private final ArticleRepository articleRepository;

    public List<Article> selectAll() {
        return articleRepository.findAll();
    }

    public Article selectById(Long id) {
        return articleRepository.findById(id)
                .orElseThrow(() -> new IllegalArgumentException("not found: " + id));
    } 

    public Article insert(RequestArticle requestArticle) {
        return articleRepository.save(requestArticle.toEntity());
    }

    @Transactional
    public Article update(RequestArticle requestArticle, Long id) {
        Article article = selectById(id);
        Article updateArticle = requestArticle.toEntity();

        return article.update(updateArticle);
    }

    public void deleteById(Long id) {
        Article article = selectById(id);

        articleRepository.delete(article);
    }
}

@Repository
public interface ArticleRepository extends JpaRepository<Article, Long> {}
```

## 테스트하기
Mock 테스트 
- 공식문서 : https://docs.spring.io/spring-boot/docs/1.5.2.RELEASE/reference/html/boot-features-testing.html
- 내가만든 프로젝트 : https://github.com/kimhyunso/Spring/tree/main/SpringBootWithJWT/src/test/java/com/project/hyunso/controller


```java
@SpringBootTest
@AutoConfigureMockMvc
class BlogApiControllerTest {

    @Autowired
    protected MockMvc mockMvc;

    @Autowired
    protected ObjectMapper objectMapper;

    @Autowired
    private WebApplicationContext context;

    @Autowired
    private ArticleService articleService;

    @Autowired
    private ArticleRepository articleRepository;

    @BeforeEach
    public void mockMvcSetUp(){
        this.mockMvc = MockMvcBuilders.webAppContextSetup(context)
                .build();
    }

    @DisplayName("findAllArticles: Article들을 조회에 성공한다.")
    @Test
    void findAllArticles() throws Exception {
        // given
        final String url = "/api/articles";

        Article article = createDefaultArticle();

        // when
        Article saveArticle = articleRepository.save(new Article(article.getTitle(), article.getContent()));

        final ResultActions resultActions = mockMvc.perform(get(url)
                .accept(MediaType.APPLICATION_JSON));

        // then
        resultActions
                .andExpect(status().isOk())
                .andExpect(jsonPath("$[0].content").value(saveArticle.getContent()))
                .andExpect(jsonPath("$[0].title").value(saveArticle.getTitle()));
    }

    private Article createDefaultArticle() {
        return new Article("title", "content");
    }
}
```