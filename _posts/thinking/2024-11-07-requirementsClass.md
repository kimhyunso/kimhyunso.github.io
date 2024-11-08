---
title:  "변경되는 고객의 요구사항 대처"
layout: single
categories:
  - thinking
tags:
  - 생각정리
  - 요구사항 대처
  - 요구사항
---

변경되는 고객의 요구사항에 대해서 어떻게 유연하게 대처해야하는지 하단의 코드를 통해 확인해보자


## 도메인
고객의 정보를 담고 있는 데이터들

```java
public enum Gender {
    MALE, FEMALE;
}

public class Customer {
    private String name;
    private int age;
    private Gender gender;

    public Customer(int age, String name, Gender gender) {
        this.name = name;
        this.age = age;
        this.gender = gender;
    }

    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder();
        builder.append("이름 : " + name + ", ");
        builder.append("나이 : " + age + ", ");
        builder.append("성별 : " + gender.name());
        return builder.toString();
    }

    // getter, equals ...
}
```

## 요구사항

- 고객의 나이가 30대 이상인 사람들을 찾고 싶다.

```java
public class SearchCustomer {
    private List<Customer> customers;

    public SearchCustomer(List<Customer> customers) {
        this.customers = customers;
    }

    public List<Customer> searchByAge(int age) {
        List<Customer> result = new ArrayList<>();
        for (Customer customer : customers) {
            if (customer.getAge() >= age) {
                result.add(customer);
            }
        }
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        SearchCustomer searchCustomer = new SearchCustomer(init());
        // 이름 : 홍길동, 나이 : 30, 성별 : MALE
        // 이름 : 김개똥, 나이 : 35, 성별 : MALE
        searchCustomer.searchByAge(30); 
    }

    public static List<Customer> init() {
        List<Customer> customers = new ArrayList();
        customers.add(new Customer(30, "홍길동", Gender.MALE));
        customers.add(new Customer(35, "김개똥", Gender.MALE));
        customers.add(new Customer(25, "아무개", Gender.FEMALE));
        customers.add(new Customer(28, "이순신", Gender.MALE));
        customers.add(new Customer(20, "강남", Gender.FEMALE));
        customers.add(new Customer(21, "이상순", Gender.MALE));
        return customers;
    }

    public static void printCustomer(List<Customer> result) {
        result.forEatch(System.out::println);
    }
}
```

- 이름에 성씨가 이씨인 사람들을 찾고 싶다.

```java
public class SearchCustomer {
    private List<Customer> customers;

    public SearchCustomer(List<Customer> customers) {
        this.customers = customers;
    }
    
    public List<Customer> searchByAge(int age) {
        List<Customer> result = new ArrayList<>();
        for (Customer customer : customers) {
            if (customer.getAge() >= age) {
                result.add(customer);
            }
        }
        return result;
    }

    public List<Customer> searchByName(String name) {
        List<Customer> result = new ArrayList<>();
        for (Customer customer : customers) {
            if (customer.getName().startsWith(name)) {
                result.add(customer);
            }
        } 
        return result;
    }
}


public class Main {
    public static void main(String[] args) {
        SearchCustomer searchCustomer = new SearchCustomer(init());
        // 이름 : 이순신, 나이 : 28, 성별 : MALE
        // 이름 : 이상순, 나이 : 21, 성별 : MALE
        searchCustomer.searchByName("이"); 
    }

    public static List<Customer> init() {
        List<Customer> customers = new ArrayList();
        customers.add(new Customer(30, "홍길동", Gender.MALE));
        customers.add(new Customer(35, "김개똥", Gender.MALE));
        customers.add(new Customer(25, "아무개", Gender.FEMALE));
        customers.add(new Customer(28, "이순신", Gender.MALE));
        customers.add(new Customer(20, "강남", Gender.FEMALE));
        customers.add(new Customer(21, "이상순", Gender.MALE));
        return customers;
    }

    public static void printCustomer(List<Customer> result) {
        result.forEatch(System.out::println);
    }
}
```

- 여성 회원인 경우만 확인하고 싶다.

```java
public class SearchCustomer {
    private List<Customer> customers;

    public SearchCustomer(List<Customer> customers) {
        this.customers = customers;
    }
    
    public List<Customer> searchByAge(int age) {
        List<Customer> result = new ArrayList<>();
        for (Customer customer : customers) {
            if (customer.getAge() >= age) {
                result.add(customer);
            }
        }
        return result;
    }

    public List<Customer> searchByName(String name) {
        List<Customer> result = new ArrayList<>();
        for (Customer customer : customers) {
            if (customer.getName().startsWith(name)) {
                result.add(customer);
            }
        } 
        return result;
    }

    public List<Customer> searchByGender(Gender gender) {
        List<Customer> result = new ArrayList<>();
        for (Customer customer : customers) {
            if (customer.getGender().equals(gender)) {
                result.add(customer);
            }
        } 
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        SearchCustomer searchCustomer = new SearchCustomer(init());
        // 이름 : 아무개, 나이 : 25, 성별 : FEMALE
        // 이름 : 강남, 나이 : 20, 성별 : FEMALE
        searchCustomer.searchByGender(Gender.FEMALE); 
    }

    public static List<Customer> init() {
        List<Customer> customers = new ArrayList();
        customers.add(new Customer(30, "홍길동", Gender.MALE));
        customers.add(new Customer(35, "김개똥", Gender.MALE));
        customers.add(new Customer(25, "아무개", Gender.FEMALE));
        customers.add(new Customer(28, "이순신", Gender.MALE));
        customers.add(new Customer(20, "강남", Gender.FEMALE));
        customers.add(new Customer(21, "이상순", Gender.MALE));
        return customers;
    }  

    public static void printCustomer(List<Customer> result) {
        result.forEatch(System.out::println);
    }
}
```


## 유연한 변화
위의 코드들은 고객의 요구사항에 대해 함수를 하나하나씩 추가하고 있다.

이것을 어떠한 요구사항에도 변경가능하게끔 만들 수는 없을까? 아래의 코드를 보자.

```java
public interface SearchFilter {
    boolean isMatch(Customer customer);
}

public class SearchCustomer {
    private List<Customer> customers;

    public SearchCustomer(List<Customer> customers) {
        this.customers = customers;
    }

    public List<Customer> search(SearchFilter filter) {
        List<Customer> result = new ArrayList<>();
        for (Customer customer : customers) {
            if (filter.isMatch(customer)) {
                result.add(customer);
            }
        }
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        SearchCustomer searchCustomer = new SearchCustomer(init());
        
        // 익명함수
        // 이름 : 홍길동, 나이 : 30, 성별 : MALE
        // 이름 : 김개똥, 나이 : 35, 성별 : MALE
        List<Customer> result = searchCustomer.search(new SearchFilter() {
            @Override
            public boolean isMatch(Customer customer) {
                return customer.getAge() >= 30;
            }
        });

        // 람다
        // 이름 : 이순신, 나이 : 28, 성별 : MALE
        // 이름 : 이상순, 나이 : 21, 성별 : MALE
        List<Customer> result = searchCustomer.search(customer -> customer.getGender().equals(Gender.MALE) && customer.getAge() < 30);

        printCustomer(result);
    }

    public static List<Customer> init() {
        List<Customer> customers = new ArrayList();
        customers.add(new Customer(30, "홍길동", Gender.MALE));
        customers.add(new Customer(35, "김개똥", Gender.MALE));
        customers.add(new Customer(25, "아무개", Gender.FEMALE));
        customers.add(new Customer(28, "이순신", Gender.MALE));
        customers.add(new Customer(20, "강남", Gender.FEMALE));
        customers.add(new Customer(21, "이상순", Gender.MALE));
        return customers;
    }  

    public static void printCustomer(List<Customer> result) {
        result.forEatch(System.out::println);
    }
}
```

- **흔히 Main메소드를 client라고 부른다.**

이와 같이 하나의 인터페이스를 추가함으로써, 어떠한 조건이든 클라이언트의 요구사항에 따라 유연하게 데이터를 제공할 수 있게 되었다.

마지막으로 `stream()`을 사용하여 마지막 리팩토링 작업을 하겠다. 아래의 코드를 보자.

```java
@FunctionalInterface
public interface SearchFilter {
    boolean isMatch(Customer customer);
}

public class SearchCustomer {
    private List<Customer> customers;

    public SearchCustomer(List<Customer> customers) {
        this.customers = customers;
    }

    public List<Customer> search(SearchFilter filter) {
        return customers.stream()
                .filter(filter::isMatch())
                .collect(Collectors.toList());
    }
}

public class Main {
    public static void main(String[] args) {
        SearchCustomer searchCustomer = new SearchCustomer(init());
        
        // 람다
        // 이름 : 이순신, 나이 : 28, 성별 : MALE
        // 이름 : 이상순, 나이 : 21, 성별 : MALE
        List<Customer> result = searchCustomer.search(customer -> customer.getGender().equals(Gender.MALE) && customer.getAge() < 30);

        printCustomer(result);
    }

    public static List<Customer> init() {
        List<Customer> customers = new ArrayList();
        customers.add(new Customer(30, "홍길동", Gender.MALE));
        customers.add(new Customer(35, "김개똥", Gender.MALE));
        customers.add(new Customer(25, "아무개", Gender.FEMALE));
        customers.add(new Customer(28, "이순신", Gender.MALE));
        customers.add(new Customer(20, "강남", Gender.FEMALE));
        customers.add(new Customer(21, "이상순", Gender.MALE));
        return customers;
    }  

    public static void printCustomer(List<Customer> result) {
        result.forEatch(System.out::println);
    }
}
```

해당 코드들을 보고 생각한 후, 언제든 바뀔 수 있는 요구사항에 대해 더욱더 유연하게 대처할 수 있도록 대비하자!
