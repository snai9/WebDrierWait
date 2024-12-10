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



### 2. 隐式等待
- json.load() 函数用于从文件中读取JSON格式的数据。该函数是 json 模块的一部分，需要先导入该模块
- json.load() 只能用于读取文件，如果你需要处理字符串形式的JSON数据，应该使用 json.loads() 函数。



### 3. 显式等待
- 用于将 Python 对象编码成 JSON 格式，并写入到文件中。
- data：要序列化的 Python 数据结构（通常是字典或列表）。
- f：一个文件对象，用于写入JSON数据。文件对象应该以写入模式打开（即 'w'）。
- ensure_ascii：默认值为 True，如果设置为 False，则允许 JSON 字符串中包含非ASCII字符。
- indent：用于美化输出的缩进级别。如果设置为 None 或 0，则输出的JSON数据不会进行格式化（即没有缩进和换行）。如果设置为正整数，则输出的JSON数据会根据该缩进级别进行格式化。



### 4. 显式等待自定义
- 用bools来取得是还是否，不需要用if来判断，基本的内置函数巧妙使用



