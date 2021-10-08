# 6登录和拦截器

## 目录

- #### 登录

- #### 拦截器

------

## 登录

### 代码：

**页面：**

```html
	<form class="form-signin" action="dashboard.html" th:action="@{/user/login}" method="post">
	<img class="mb-4" th:src="@{/asserts/img/bootstrap-solid.svg}" src="asserts/img/bootstrap-solid.svg" alt="" width="72" height="72">
	<h1 class="h3 mb-3 font-weight-normal" th:text="#{login.tip}">Please sign in</h1>
		<!-- 判断 提示信息-->
	<p style="color: red" th:text="${msg}" th:if="${not #strings.isEmpty(msg)}"></p>
	<label class="sr-only">Username</label>
	<input type="text"  name="username" class="form-control" th:placeholder="#{login.username}" placeholder="Username" required="" autofocus="">
	<label class="sr-only">Password</label>
	<input type="password" name="password" class="form-control" th:placeholder="#{login.password}" placeholder="Password" required="">
	<div class="checkbox mb-3">
		<label>
			<input type="checkbox" value="remember-me"> [[#{login.remember}]]
		</label>
	</div>
	<button class="btn btn-lg btn-primary btn-block" type="submit" th:text="#{login.btn}">Sign in</button>
	<p class="mt-5 mb-3 text-muted">© 2017-2018</p>
	<a class="btn btn-sm" th:href="@{/index.html(l='zh_CN')}">中文</a>
	<a class="btn btn-sm" th:href="@{/index(l='en_US')}">English</a>
</form>
```



**控制器：**

```java
@Controller
public class LoginController {

//    @GetMapping
//    @PutMapping
//    @DeleteMapping

//    @RequestMapping(value = "/user/login",method = RequestMethod.POST)
    @PostMapping("/user/login") //这个达到的效果和用上面的RequestMapping效果一样
    public String login(@RequestParam("username") String username, @RequestParam("password") String password, Map<String,Object> map, HttpSession session){

        if(!StringUtils.isEmpty(username)&& "123456".equals(password))
        {
//            return "dashboard";
            session.setAttribute("loginUser",username);
            //登录成功 防止表单重复提交 用重定向到主页
            return "redirect:/main.html";
        }else{
            //登录失败\
            map.put("msg","用户名或密码错误");
            return "login";
        }

    }
}
```

### 技巧：

开发期间模板引擎页面修改以后，要**实时生效**

**1）、禁用模板引擎的缓存**

```properties
# 禁用缓存
spring.thymeleaf.cache=false 
```

**2）、页面修改完成以后ctrl+f9：重新编译；**



**登陆错误消息的显示**

```html
<p style="color: red" th:text="${msg}" th:if="${not #strings.isEmpty(msg)}"></p>
```

------

## 拦截器

### 拦截器类：

```java

/**
 * 登陆检查，
 */
public class LoginHandlerInterceptor implements HandlerInterceptor {
    //目标方法执行之前
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        Object user = request.getSession().getAttribute("loginUser");
        if(user == null){
            //未登陆，返回登陆页面
            request.setAttribute("msg","没有权限请先登陆");
            request.getRequestDispatcher("/index.html").forward(request,response);
            return false;
        }else{
            //已登陆，放行请求
            return true;
        }

    }

    @Override
    public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView) throws Exception {

    }

    @Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) throws Exception {

    }
}

```

### 注册拦截器

```java
 //所有的WebMvcConfigurerAdapter组件都会一起起作用
    @Bean //将组件注册在容器
    public WebMvcConfigurerAdapter webMvcConfigurerAdapter(){
        WebMvcConfigurerAdapter adapter = new WebMvcConfigurerAdapter() {
            @Override
            public void addViewControllers(ViewControllerRegistry registry) {
                registry.addViewController("/").setViewName("login");
                registry.addViewController("/index.html").setViewName("login");
                registry.addViewController("/main.html").setViewName("dashboard");
            }

            //注册拦截器
            @Override
            public void addInterceptors(InterceptorRegistry registry) {
                //super.addInterceptors(registry);
                //静态资源；  *.css , *.js
                //SpringBoot已经做好了静态资源映射
                registry.addInterceptor(new LoginHandlerInterceptor()).addPathPatterns("/**")
                        .excludePathPatterns("/index.html","/","/user/login");
            }
        };
        return adapter;
    }
```

