import re

key = '''$(".jp-title").click(function(){
                                        $(".help").slideToggle();
                                    });
                                    $(".jp-download").click(function(){
                                        window.open('/e/action/down.php?classid=12543&id=325707&mp3=http://mp3.en8848.com/kouyu/useful1000/01.mp3') ;
                                    });
                                    $(".anniu").click(function(){
                                        $(".download").hide();
                                    });'''

# 表达式
# \$\("\.jp-download"\)\.click\(function\(\){\s.*window\.open\('\S.*
p = '\$\("\.jp-download"\)\.click\(function\(\){\s.*window\.open\(\S.*'
# p = 'html'
# 我们在编译这段正则表达式
pattern = re.compile(p)
# 在源文本中搜索符合正则表达式的部分
matcher1 = re.search(pattern, key)
# 打印出来
if not matcher1 == 'none':
    split = matcher1[0].split('\'')[1]
    urlTmp = 'http://www.en8848.com.cn' + split
    print(urlTmp)



# http://www.en8848.com.cn/e/action/down.php?classid=12543&id=325707&mp3=http://mp3.en8848.com/kouyu/useful1000/01.mp3
