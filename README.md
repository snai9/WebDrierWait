# 通过写一些简单的功能来学习Python的基础用法



##
### Selenium 是一个用于自动化Web应用程序测试的工具，支持多种浏览器和编程语言。    
各种浏览器的驱动按版本下载：
[谷歌浏览器](https://registry.npmmirror.com/binary.html?path=chromedriver/)
[EDGE浏览器](https://registry.npmmirror.com/binary.html?path=edgedriver/)
[火狐浏览器](https://registry.npmmirror.com/binary.html?path=geckodriver/)  
```python
from selenium import webdriver

# 创建 WebDriver 对象，启动浏览器
driver = webdriver.Chrome()

# 打开网页
driver.get("http://example.com")

# 定位元素并进行操作
element = driver.find_element_by_id("some-id")
element.click()

# 关闭浏览器
driver.quit()
```


## 自动化测试中的等待

### 强制等待（Sleep）
#### 用法：
- 强制等待是通过time.sleep()函数实现的，它会暂停代码执行指定的时间（以秒为单位）。例如：

```python
import time
time.sleep(5)  # 强制等待5秒
```
#### 原理：
- 强制等待实际上是让执行线程休眠指定的时间，期间不进行任何操作。

#### 源码分析：
- time.sleep()函数是Python标准库time模块提供的一个函数，用于暂停程序执行指定的秒数。

#### 相同点与不同点：

- 相同点： 强制等待是最简单的等待方式，适用于一些固定时间的等待需求。
- 不同点： 强制等待不智能，不会检查元素是否已经加载完成，只是简单地等待固定时间，可能会导致不必要的等待或者错过元素加载完成的最佳时机。




### 隐式等待（Implicitly Wait）
#### 用法：
- 隐式等待是全局设置的，对WebDriver实例的所有查找操作生效。例如：

```python
driver.implicitly_wait(10)  # 设置隐式等待时间为10秒
```
#### 原理：
- 隐式等待会在查找元素时，如果元素未立即可用，WebDriver会等待一定的时间再去查找元素。

#### 源码分析：
- 隐式等待是通过WebDriver的implicitly_wait方法设置的，它会在WebDriver实例的整个生命周期内起作用。

#### 相同点与不同点：

- 相同点： 隐式等待会在元素未立即可用时等待一定的时间。
- 不同点： 隐式等待是全局性的，对所有元素查找操作生效，而不会针对特定元素。如果页面某些JS加载慢，但所需元素已经加载完成，隐式等待仍会等待页面全部加载完成。




### 显式等待（Explicit Wait）
#### 用法：
- 显式等待是针对特定条件的等待，直到条件满足或超时。例如：

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, 'myElement')))
```
#### 原理：
- 显式等待通过WebDriverWait对象和expected_conditions来实现，它会周期性地检查某个条件是否满足，直到条件满足或超时。

#### 源码分析：
- WebDriverWait类在构造时接受WebDriver实例、超时时间和其他参数，until方法会定期调用传入的条件方法，直到返回值不为False或空。

#### 相同点与不同点：

- 相同点： 显式等待和隐式等待都是在设定的超时时间内不断轮询判断是否满足条件要求。
- 不同点： 显式等待是针对特定元素的等待，可以为每个操作设置不同的等待条件和时间，更加灵活和精确。而隐式等待是全局性的，对所有元素查找操作生效。



### 4. 显式等待自定义
- 用bools来取得是还是否，不需要用if来判断，基本的内置函数巧妙使用



