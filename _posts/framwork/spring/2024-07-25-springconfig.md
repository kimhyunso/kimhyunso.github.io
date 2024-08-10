---
title:  "스프링 부트 - BatchConfiguration"
layout: single
categories:
    - spring
tags:
    - 스프링 부트
    - Batch
---

## SpringBatch 시작

```java
@SpringBootApplication
@RequiredArgsConstructor
@EnableBatchProcessing
public class LinkedinBatchApplication implements CommandLineRunner {

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

## `@Configuration`
로그를 보면 Job보다 Step이 먼저 실행된다. `JobParamters`가 정상적으로 나온다.

![Configuration로그](https://github.com/user-attachments/assets/70144908-81ef-40b8-8d52-57ac32eb728f)
{: .align-center}

```java
@Configuration
public class ConfigJob {

    @Bean
    public Job configTestJob(JobRepository jobRepository, PlatformTransactionManager transactionManager) {
        return new JobBuilder("configTestJob", jobRepository)
                .start(configTestStep(jobRepository, transactionManager, null, null))
                .build();
    }

    @Bean
    @JobScope
    public Step configTestStep(JobRepository jobRepository, PlatformTransactionManager transactionManager,
                               @Value("#{jobParameters[item]}") String item,
                               @Value("#{jobParameters[type]}") String type) {
        return new StepBuilder("configTestStep", jobRepository)
                .tasklet(configTestTasklet(item, type), transactionManager)
                .build();
    }

    public Tasklet configTestTasklet(String item, String type) {
        return (contribution, chunkContext) -> {
            System.out.println(item);
            System.out.println(type);
            return RepeatStatus.FINISHED;
        };
    }
}
```

## `@Component`
로그를 보면 Job이 Step보다 먼저 실행된다. `JobParamters`가 `null`이 나온다.

![Component로그](https://github.com/user-attachments/assets/ad5b866d-fc30-4576-ae77-d3b167ad8bdc)
{: .align-center}

```java
@Component
public class ConfigJob {

    @Bean
    public Job configTestJob(JobRepository jobRepository, PlatformTransactionManager transactionManager) {
        return new JobBuilder("configTestJob", jobRepository)
                .start(configTestStep(jobRepository, transactionManager, null, null))
                .build();
    }

    @Bean
    @JobScope
    public Step configTestStep(JobRepository jobRepository, PlatformTransactionManager transactionManager,
                               @Value("#{jobParameters[item]}") String item,
                               @Value("#{jobParameters[type]}") String type) {
        return new StepBuilder("configTestStep", jobRepository)
                .tasklet(configTestTasklet(item, type), transactionManager)
                .build();
    }

    public Tasklet configTestTasklet(String item, String type) {
        return (contribution, chunkContext) -> {
            System.out.println(item);
            System.out.println(type);
            return RepeatStatus.FINISHED;
        };
    }
}
```











