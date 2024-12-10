# 通过写一些简单的功能来学习Python的基础用法
***


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
---



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
---



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
---


### 显式等待自定义

#### 在自定义显式等待的条件函数时，返回值的规定如下：

- 返回值必须能够被评估为布尔值：条件函数应该返回一个值，该值在布尔上下文中被评估为True或False。如果函数返回True，until方法会停止等待并返回该值；如果返回False，则继续等待直到超时
- 返回实际需要的对象：除了返回布尔值外，条件函数也可以返回实际需要的对象。例如，如果你正在等待一个元素变得可见，函数可以在确认元素可见后返回该元素对象
- 超时时抛出异常：如果在设定的超时时间内条件函数始终返回False，则WebDriverWait会抛出TimeoutException异常
- 异常处理：在执行条件函数的过程中，如果抛出了在WebDriverWait构造函数中指定的ignored_exceptions异常类，则这些异常会被忽略，等待会继续进行，直到超时或条件满足

#### 要编写一个自定义显式等待的条件函数来等待一个动态加载的元素，你可以遵循以下步骤：

- 定义自定义条件函数：这个函数需要接受一个driver作为参数，并返回一个布尔值，表示条件是否满足。
- 使用WebDriverWait和until方法：将自定义条件函数传递给WebDriverWait的until方法，等待直到条件满足或超时。

#### 精妙的用法
```python
def muliti_click(target_element, next_element):
    def _predicate(driver):
        driver.find_element(*target_element).click()
        return driver.find_element(*next_element)
    return _predicate
```
return driver.find_element(*next_element)上一句如果找到元素并点击后就直接返回下一个元素，  
由源码得知，即使没有找到元素也会抛出异常忽略掉，重新进入循环进行查找 ，直到找到元素才退出循环  
---

### 解包

- 在`显式等待.py`中，`*locator`的使用是Python的一种特殊语法，称为参数解包（argument unpacking）。当你在函数调用中看到*紧跟在一个变量前时，这意味着你将这个变量解包为独立的参数传递给函数。

在你提到的代码element = driver.find_element(*locator)中，locator是一个元组，其中包含了两个元素：定位策略（如By.ID）和定位值（如元素的id）。*locator将这个元组解包为两个独立的参数，分别对应find_element方法的by和value参数。这样做的好处是可以使代码更加简洁，并且能够灵活地传递参数。

具体来说，locator元组可能是这样的：(By.ID, 'some-id')，其中By.ID是定位策略，而'some-id'是具体的定位值。当你使用*locator时，它会被解包为两个参数，相当于调用driver.find_element(By.ID, 'some-id')。





