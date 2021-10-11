# 一、Spring Boot入门

## 目录

1. ##### Spring Boot 简介

2. ##### 单体应用与微服务

4. ##### Spring Boot HelloWorld

5. ##### Hello World探究

6. ##### 使用Spring Initializer快速创建Spring Boot项目

------



## Spring Boot 简介

- #### 背景

     ​    J2EE笨重的开发、繁多的配置、低下的开发效率、 复杂的部署流程、第三方技术集成难度大。 

- #### 解决方案

  - **“Spring全家桶”时代。** 

  - **Spring Boot  →  J2EE一站式解决方案** 

  - **Spring Cloud →  分布式整体解决方案**

- #### 简介

  ​    **Spring Boot来简化Spring应用开发，约定大于配置，** 

  **去繁从简，很简单几步就能创建一个独立的，产品级别的应用** 

- #### 优点

  – 快速创建独立运行的Spring项目以及与主流框架集成 
  
  – 使用嵌入式的Servlet容器，应用无需打成WAR包 
  
  – starters自动依赖与版本控制 
  
  – 大量的自动配置，简化开发，也可修改默认值 
  
  – 无需配置XML，无代码生成，开箱即用 
  
  – 准生产环境的运行时应用监控 
  
  – 与云计算的天然集成
------

##   单体应用和微服务

- #### 单体应用

  ​	正如我们平常所开发的小型项目一样，所有的模块与功能都集成在一个项目中（ALL IN ONE），但随着业务的不断发展单体应用会越来越庞大；若是为了达到高并发的效果可能是将该单体项目在多台主机上运行，然后使用nigx等来进行负载均衡操作。

- #### 微服务

    每一个功能元素最终都是一个可独立替换和独立升级的软件单元；可以根据项目需求利用每个独立的单元模块进行整合。

------

## Spring Boot HelloWord

1. #### 使用Maven创建项目

2. #### 在相关的pom文件加入以下代码

   ```xml
    <parent>
           <groupId>org.springframework.boot</groupId>
           <artifactId>spring-boot-starter-parent</artifactId>
           <version>2.2.0.RELEASE</version>
       </parent>
       <dependencies>
           <dependency>
               <groupId>org.springframework.boot</groupId>
               <artifactId>spring-boot-starter-web</artifactId>
            </dependency>
       </dependencies>
    <!-- 这个插件，可以将应用打包成一个可执行的jar包；-->
    <!-- 将这个应用打成jar包，直接使用java -jar的命令进行执行；-->
       <build>
           <plugins>
               <plugin>
                   <groupId>org.springframework.boot</groupId>
                   <artifactId>spring-boot-maven-plugin</artifactId>
               </plugin>
           </plugins>
       </build>
   ```

3. #### 编写SpringBoot主程序 ，用来启动程序

   ```java
   /**
    *  @SpringBootApplication 来标注一个主程序类，说明这是一个Spring Boot应用
    */
   @SpringBootApplication
   public class Main {
       public static void main(String[] args) {
           // Spring应用启动起来 注意这里传入的参数 分别是类名.class和args
           SpringApplication.run(Main.class,args);
       }
   }
   ```

   

4. #### 编写相关的Controller、Service类

   ```java
   @Controller
   public class HelloController {
   
       @ResponseBody
       @RequestMapping("/hello")
       public String hello(){
           return "Hello World!";
       }
   }
   ```

------

## Hello World探究

### 1、POM文件

#### 1、父项目

```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.2.0.RELEASE</version>
</parent>

他的父项目是
<parent>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-dependencies</artifactId>
  <version>2.2.0.RELEASEE</version>
  <relativePath>../../spring-boot-dependencies</relativePath>
</parent>
他来真正管理Spring Boot应用里面的所有依赖版本；

```

Spring Boot的版本仲裁中心；

以后我们导入依赖默认是不需要写版本；（没有在dependencies里面管理的依赖自然需要声明版本号）

#### 2、启动器

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```

**spring-boot-starter**-==web==：

​	spring-boot-starter：spring-boot场景启动器；帮我们导入了web模块正常运行所依赖的组件；



Spring Boot将所有的功能场景都抽取出来，做成一个个的starters（启动器），只需要在项目里面引入这些starter相关场景的所有依赖都会导入进来。要用什么功能就导入什么场景的启动器



### 2、主程序类，主入口类

```java
/**
 *  @SpringBootApplication 来标注一个主程序类，说明这是一个Spring Boot应用
 */
@SpringBootApplication
public class Main {
    public static void main(String[] args) {
        // Spring应用启动起来 注意这里传入的参数 分别是类名.class和args
        SpringApplication.run(Main.class,args);
    }
}

```

@**SpringBootApplication**:    Spring Boot应用标注在某个类上说明这个类是SpringBoot的主配置类，SpringBoot就应该运行这个类的main方法来启动SpringBoot应用；



```java
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Inherited
@SpringBootConfiguration
@EnableAutoConfiguration
@ComponentScan(excludeFilters = {
      @Filter(type = FilterType.CUSTOM, classes = TypeExcludeFilter.class),
      @Filter(type = FilterType.CUSTOM, classes = AutoConfigurationExcludeFilter.class) })
public @interface SpringBootApplication {
```

@**SpringBootConfiguration**:Spring Boot的配置类；

​		标注在某个类上，表示这是一个Spring Boot的配置类；

​		@**Configuration**:配置类上来标注这个注解；

​			**配置类** -----  **配置文件**；**配置类也是容器中的一个组件**；@Component

@**EnableAutoConfiguration**：开启自动配置功能；

​		以前我们需要配置的东西，Spring Boot帮我们自动配置；@**EnableAutoConfiguration**告诉SpringBoot开启自动配置功能；这样自动配置才能生效；

```java
@AutoConfigurationPackage
@Import(EnableAutoConfigurationImportSelector.class)
public @interface EnableAutoConfiguration {
```

​      	@**AutoConfigurationPackage**：自动配置包

​		@**Import**(AutoConfigurationPackages.Registrar.class)：

​		Spring的底层注解@Import，给容器中导入一个组件；导入的组件由AutoConfigurationPackages.Registrar.class；

==将主配置类（@SpringBootApplication标注的类）的所在包及下面所有子包里面的所有组件扫描到Spring容器；==

​	@**Import**(EnableAutoConfigurationImportSelector.class)；

​		给容器中导入组件？

​		**EnableAutoConfigurationImportSelector**：导入哪些组件的选择器；

​		将所有需要导入的组件以全类名的方式返回；这些组件就会被添加到容器中；

​		会给容器中导入非常多的自动配置类（xxxAutoConfiguration）；就是给容器中导入这个场景需要的所有组件，并配置好这些组件；	

有了自动配置类，免去了我们手动编写配置注入功能组件等的工作；

​		SpringFactoriesLoader.loadFactoryNames(EnableAutoConfiguration.class,classLoader)；



==Spring Boot在启动的时候从类路径下的META-INF/spring.factories中获取EnableAutoConfiguration指定的值，将这些值作为自动配置类导入到容器中，自动配置类就生效，帮我们进行自动配置工作；==以前我们需要自己配置的东西，自动配置类都帮我们；

J2EE的整体整合解决方案和自动配置都在spring-boot-autoconfigure-2.2.0.RELEASE.jar；



## 使用Spring Initializer快速创建Spring Boot项目

### IDEA：使用 Spring Initializer快速创建项目

IDE都支持使用Spring的项目创建向导快速创建一个Spring Boot项目；

选择我们需要的模块；向导会联网创建Spring Boot项目；

默认生成的Spring Boot项目；

- 主程序已经生成好了，我们只需要我们自己的逻辑
- resources文件夹中目录结构
  - static：保存所有的静态资源； js css  images；
  - templates：保存所有的模板页面；（Spring Boot默认jar包使用嵌入式的Tomcat，默认不支持JSP页面）；可以使用模板引擎（freemarker、thymeleaf）；
  - application.properties：Spring Boot应用的配置文件；可以修改一些默认设置；