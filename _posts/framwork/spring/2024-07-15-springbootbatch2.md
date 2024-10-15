---
title:  "스프링 부트 - Batch 두번째"
layout: single
categories:
    - spring
tags:
    - 스프링 부트
    - 스프링 배치
---

## 공식문서
https://docs.spring.io/spring-batch/reference/index.html


## `@Configuration`, `@Component` 차이점

```java
@SpringBootApplication
@RequiredArgsConstructor
@EnableBatchProcessing
public class BatchApplication implements CommandLineRunner {

	private final JobLauncher jobLauncher;
	private final JobRegistry jobRegistry;

	public static void main(String[] args) {
		SpringApplication.run(LinkedinBatchApplication.class, args);
	}

	@Override
	public void run(String... args) throws Exception {
		JobParameters jobParameters = new JobParametersBuilder()
				.addString("item", "shoes")
				.addString("type", "roses")
				.toJobParameters();

		Job job = jobRegistry.getJob("configTestJob");
		jobLauncher.run(job, jobParameters);
	}
}
```

### `@Configuration`
로그를 보면 Job보다 Step이 먼저 실행된다. `JobParamters`가 정상적으로 나온다.

![Configuration로그](https://github.com/user-attachments/assets/70144908-81ef-40b8-8d52-57ac32eb728f)
{: .align-center}

```java
@Configuration
public class ConfigJob {
    private final JobRepository jobRepository;
    private final PlatformTransactionManager transactionManager;

    @Bean
    public Job componentJob() {
        return new JobBuilder("componentJob", jobRepository)
                .start(componentStep(jobRepository, transactionManager, null, null))
                .build();
    }

    @Bean
    @JobScope
    public Step componentStep(@Value("#{jobParameters[item]}") String item,
                               @Value("#{jobParameters[type]}") String type) {

        return new StepBuilder("configTestStep", jobRepository)
                .tasklet(componentTasklet(item, type), transactionManager)
                .build();
    }

    public Tasklet componentTasklet(String item, String type) {
        return (contribution, chunkContext) -> {
            System.out.println("아이템 : " + item + "\t" + " 아이템의 유형 : " + type);
            return RepeatStatus.FINISHED;
        };
    }
}
```

### `@Component`
로그를 보면 Job이 Step보다 먼저 실행된다. `JobParamters`가 `null`이 나온다.

![Component로그](https://github.com/user-attachments/assets/ad5b866d-fc30-4576-ae77-d3b167ad8bdc)
{: .align-center}

```java
@Component
@RequiredArgsConstructor
public class ConfigJob {
    private final JobRepository jobRepository;
    private final PlatformTransactionManager transactionManager;

    @Bean
    public Job componentJob() {
        return new JobBuilder("componentJob", jobRepository)
                .start(componentStep(jobRepository, transactionManager, null, null))
                .build();
    }

    @Bean
    @JobScope
    public Step componentStep(@Value("#{jobParameters[item]}") String item,
                               @Value("#{jobParameters[type]}") String type) {

        return new StepBuilder("configTestStep", jobRepository)
                .tasklet(componentTasklet(item, type), transactionManager)
                .build();
    }

    public Tasklet componentTasklet(String item, String type) {
        return (contribution, chunkContext) -> {
            System.out.println("아이템 : " + item + "\t" + " 아이템의 유형 : " + type);
            return RepeatStatus.FINISHED;
        };
    }
}
```

## 메타테이블 분리
- `@Primary`: 주된 bin으로 설정하는 것
- `@Qualifier(binName)`: binName으로 설정된 bin을 주입 

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



