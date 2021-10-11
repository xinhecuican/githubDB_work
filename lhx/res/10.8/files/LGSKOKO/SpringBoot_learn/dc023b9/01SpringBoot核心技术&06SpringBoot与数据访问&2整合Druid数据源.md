# 2、整合Druid数据源

## 目录

- #### 配置文件

- #### 配置类

## 配置文件

```xml
 <dependency>
 	<groupId>com.alibaba</groupId>
 	<artifactId>druid</artifactId>
 	<version>1.1.8</version>
 </dependency>
```

```properties
spring:
  datasource:
    username: root
    password: 123456
    url: jdbc:mysql://localhost:3306/dormitory
    driver-class-name: com.mysql.jdbc.Driver
  

    #   数据源其他配置
    initialSize: 5
    minIdle: 5
    maxActive: 20
    maxWait: 60000
    timeBetweenEvictionRunsMillis: 60000
    minEvictableIdleTimeMillis: 300000
    validationQuery: SELECT 1 FROM DUAL
    testWhileIdle: true
    testOnBorrow: false
    testOnReturn: false
    poolPreparedStatements: true
#    schema:
#      - classpath:department.sql
```



## 配置类

```java
导入druid数据源
@Configuration
public class DruidConfig {
    @ConfigurationProperties(prefix="spring.datasource")
    @Bean
    public DataSource druid(){
        return new DruidDataSource();
    }

    //配置Druid的监控
    //1、配置一个管理后台的Servlet
    @Bean
    public ServletRegistrationBean statViewServlet(){
        ServletRegistrationBean bean = new ServletRegistrationBean(new StatViewServlet(),"/druid/*");
        Map<String,String> initParams = new HashMap<>();

        initParams.put("loginUsername","admin");
        initParams.put("loginPassword","123456");
        initParams.put("allow","");//默认是允许所有访问
        initParams.put("deny","192.168.15.21");

        bean.setInitParameters(initParams);
        return bean;
    }

    //2、配置一个web监控的filter
    @Bean
    public FilterRegistrationBean webStatFilter(){
        FilterRegistrationBean bean = new FilterRegistrationBean();
        bean.setFilter(new WebStatFilter());

        Map<String,String> initParams = new HashMap<>();
        initParams.put("exclusions","*.js,*.css,/druid/*");//哪些不用拦截

        bean.setInitParameters(initParams);

        bean.setUrlPatterns(Arrays.asList("/*"));//拦截规则
        return bean;
    }

}
```

## 