---
title:  "스프링 부트 - Batch"
layout: single
categories:
    - spring
tags:
    - 스프링 부트
    - 스프링 배치
---

## 공식문서
https://docs.spring.io/spring-batch/reference/index.html

## 배치작업
대량의 작업을 한 번에 `일괄처리` 할 수 있도록 도와주는 작업

## 스케쥴링
어떠한 작업을 `특정 시간`에 작업을 실행하도록 도와주는 설정

## Batch
- 하나의 Job은 여러개의 Step을 가질 수 있으며 하나의 Step은 `ItemReader`, `ItemProcessor`, `ItemWriter`를 가질 수 있다. 
- `JobLauncher`, `Job`, `Step`은 `JobRepository`와 상호작용하며 배치 메타 테이블과 서로 상호작용을 하게 된다.

배치 프로그램은 두 가지 형태의 `Step`을 구성할 수 있다.
1. Tasklet-based Step
2. Chunk-based Step

![배치아키텍처](https://github.com/user-attachments/assets/c84c735c-9dfd-4c80-8905-a99b09a0163b)
{: .align-center}


## 메타테이블 분리
```java
@Configuration
public class DataSourceConfig {

    @Primary
    @Bean(name = "dataSource")
    public DataSource applicationDataSource( @Value("${spring.datasource.driver-class-name}") String driverClassName,
                                             @Value("${spring.datasource.url}") String url,
                                             @Value("${spring.datasource.username}") String username,
                                             @Value("${spring.datasource.password}") String password) {
        return DataSourceBuilder.create()
                .driverClassName(driverClassName)
                .url(url)
                .username(username)
                .password(password)
                .build();
    }

    @Bean(name = "subDataSource")
    public DataSource batchDataSource() {
        return new EmbeddedDatabaseBuilder()
                .setType(EmbeddedDatabaseType.H2)
                .addScript("/org/springframework/batch/core/schema-h2.sql")
                .generateUniqueName(true)
                .build();
    }



    @Bean
    public JobRepository jobRepository(@Qualifier("subDataSource") DataSource dataSource, PlatformTransactionManager transactionManager) throws Exception {
        JobRepositoryFactoryBean factory = new JobRepositoryFactoryBean();
        factory.setDataSource(dataSource);
        factory.setTransactionManager(transactionManager);
        factory.afterPropertiesSet();
        return factory.getObject();
    }

}
```



## Tasklet-based Step
















