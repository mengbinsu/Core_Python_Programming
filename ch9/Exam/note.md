## 练习
#### 9.1 文件过滤. 显示一个文件的所有行, 忽略以井号( # )开头的行. 这个字符被用做 Python , Perl, Tcl, 等大多脚本文件的注释符号. 附加题: 处理不是第一个字符开头的注释.
	#!/usr/bin/env python
	f = open('test.txt')
	for line in f:
	    if line is not None and line[0] != '#':
	        print line,
	f.close()

#### 9.2 文件访问. 提示输入数字 N 和文件 F, 然后显示文件 F 的前 N 行.
    #!/usr/bin/env python
	f = open('test.txt')
	for line in f:
	    if line is not None and line[0] != '#':
	        print line,
	f.close()

#### 9.3 文件信息. 提示输入一个文件名, 然后显示这个文本文件的总行数.
	#!/usr/bin/env python
	print sum([1 for eachLine in open(raw_input('Input FileName:'))])
#### 9.4 文件访问. 写一个逐页显示文本文件的程序. 提示输入一个文件名, 每次显示文本文件的 25 行, 暂停并向用户提示"按任意键继续", 按键后继续执行. 
    #!/usr/bin/env python

	fileName = raw_input('FileName: ')
	lineNum = 0
	f = open(fileName)
	for eachLine in f:
	    if lineNum % 2 == 0 and lineNum > 0:
	        if(len(raw_input('Enter any key to continue...'))):
	            continue
	    lineNum += 1
	    print '%2d ' %lineNum, eachLine
	f.close()
#### 9.8 模块研究. 提取模块的属性资料. 提示用户输入一个模块名(或者从命令行接受输入). 然后使用 dir() 和其它内建函数提取模块的属性, 显示它们的名字, 类型, 值.
    #!/usr/bin/env python
	import importlib
	
	def get_module_attr(module_name):
	    module = importlib.import_module(module_name)
	    attrs = dir(module)
	    res = []
	
	    for attr in attrs:
	        value = getattr(module, attr)
	        res.append({'name':attr, 'type':type(value), 'value':value})
	    return res
	
	for attr in get_module_attr('math'):
	    print 'name:%s\t type:%s\t value:%20s' %(attr['name'], attr['type'],attr['value'])
#### 9.9 Python 文档字符串. 进入 Python 标准库所在的目录. 检查每个 .py 文件看是否有 doc 字符串, 如果有, 对其格式进行适当的整理归类. 你的程序执行完毕后, 应该会生成一个漂亮的清单. 里边列出哪些模块有文档字符串, 以及文档字符串的内容. 清单最后附上那些没有文档字符串模块的名字. 附加题: 提取标准库中各模块内全部类(class)和函数的文档.
    
		#!/usr/bin/env python

		import os
		import importlib
		from warnings import catch_warnings
		
		pymodules = {}
		path = '/usr/local/lib/python2.7'
		suffix = '.py'
		
		pyfiles = [f for f in os.listdir(path) if f.endswith(suffix)]
		for f in pyfiles:
		    module_name = os.path.splitext(f)[0]
		    try:
		        module = importlib.import_module(module_name)
		        pymodules[module_name] = module.__doc__
		    except ImportError, e:
		        continue
		
		hasdoc = []
		nodoc = []
		for module in pymodules:
		    if pymodules[module]:
		        hasdoc.append(module)
		    else:
		        nodoc.append(module)
		
		print 'module has no doc:'
		for key in nodoc:
		    print key + '|'
		
		print '*' * 50
		
		print 'module has doc:'
		for key in hasdoc:
		    print '[', key, ']'
		    print pymodules[key]
		    print '-' * 30

#### 9–11. Web 站点地址.

** a) 编写一个 URL 书签管理程序. 使用基于文本的菜单, 用户可以添加, 修改或者删除书签数据项. 书签数据项中包含站点的名称, URL 地址, 以及一行简单说明(可选). 另外提供检索功能, 可以根据检索关键字在站点名称和 URL 两部分查找可能的匹配. 程序退出时把数据保存到一个磁盘文件中去; 再次执行时候加载保存的数据. **

** b)改进 a) 的解决方案, 把书签输出到一个合法且语法正确的 HTML 文件(.html 或 htm )中, 这样用户就可以使用浏览器查看自己的书签清单. 另外提供创建"文件夹"功能, 对相关的书签进行 分组管理. **

**附加题: 请阅读 Python 的 re 模块了解有关正则表达式的资料, 使用正则表达式对用户输入 的 URL 进行验证**
	#!/usr/bin/env python
	
	import re, os
	
	def checkurl(url):
	    regex = re.compile(
	            r'^(?:http|ftp)s?://'  # http:// or https://
	            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
	            r'localhost|'  # localhost...
	            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
	            r'(?::\d+)?'  # optional port
	            r'(?:/?|[/?]\S+)$', re.IGNORECASE
	            )
	    if regex.match(url):
	        return True
	    else:
	        return False
	
	
	def geturl():
	    name = raw_input('Please input a url name: ')
	    while 1:
	        url = raw_input('Please input a url address: ')
	        if checkurl(url):
	            break;
	        else:
	            print 'wrong url format, please input again'
	
	    mark = raw_input('Please input a url mark: ')
	    folder = raw_input('Please input a url folder: ')
	    return (name, url, mark, folder)
	
	def load(filename):
	    f = open(filename, 'a+')
	    bmlist = f.readlines()
	    f.close()
	    return bmlist
	
	def save(bmlist, filename):
	    f = open(filename, 'w+')
	    for line in bmlist:
	        if len(line) == 0:
	            continue
	        f.write(line)
	    f.close()
	
	def add(bmlist, name, url, mark, folder='default'):
	    bookmark = name + ';' + url + ';' + mark + ';' + folder + os.linesep
	    if bookmark not in bmlist:
	        bmlist.append(bookmark)
	
	def modify(bmlist, index, name, url, mark, folder):
	    bmlist[index] = name + ';' + url + ';' + mark + ';' + folder + os.linesep
	
	def delbm(bmlist, index):
	    bmlist.pop(index)
	
	def findbk(bmlist, fname, furl):
	    for i, item in enumerate(bmlist):
	        (name, url, mark, folder) = item.split(';')
	        if fname and furl:
	            if (fname in name) and (furl in url):
	                return i
	
	        if fname and (fname in name):
	            return i
	
	        if furl and (furl in url):
	            return i
	    else:
	        return -1
	
	def output2html(bmlist):
	    for i, item in enumerate(bmlist):
	        print item
	        (name, url, mark, folder) = item.split(';')
	        if os.access(folder.strip(), os.F_OK) == False:
	            os.mkdir(folder.strip())
	        filename = name.strip() + '.html'
	        f = open(filename, 'w+')
	        fmt = '%d\t%s\t<a href=%s>%s</a>\t%s\t%s<br>'
	        f.write('<html><head><title>bookmark</title></head><body>')
	        content = fmt %(i+1, name, r'http:\\' + url, url, mark, folder)
	        f.write(content)
	        f.write('</body></html>')
	        f.close()
	        os.rename(filename, folder.strip() + os.sep + filename)
	
	def show_menu():
	    bmlist = load(r'url.txt')
	    while True:
	        print '0. quit'
	        print '1. add a url bookmark'
	        print '2. modify a url bookmark'
	        print '3. delte a url bookmark'
	        print '4. find a url bookmark'
	        print '5. output url bookmark as html'
	        print '6. display all bookmarks'
	        print '\n'
	
	        iInput = input('Please input operation num: ')
	
	        if iInput < 0 or iInput > 6:
	            print 'Error input operation, try again.\n'
	            continue
	        elif 0 == iInput:
	            save(bmlist, r'url.txt')
	            break;
	        elif 1 == iInput:
	            data = geturl()
	            add(bmlist, *data)
	        elif 2 == iInput:
	            index = int(raw_input('bookmark index: '))
	            data = geturl()
	            modify(bmlist, index, *data)
	        elif 3 == iInput:
	            index = int(raw_input('bookmark index: '))
	            delbm(bmlist, index)
	        elif 4 == iInput:
	            name = raw_input('url name: ')
	            url = raw_input('url address: ')
	            index = findbk(bmlist, name, url)
	            if index == -1:
	                print 'not found'
	            else:
	                print bmlist[index]
	        elif 5 == iInput:
	            output2html(bmlist)
	        elif 6 == iInput:
	            for index, eachLine in enumerate(bmlist):
	                print '%2d' %index, eachLine
	
	if __name__ == '__main__':
	    show_menu()

#### 9.12 用户名和密码. 回顾练习 7-5 , 修改代码使之可以支持"上次登录时间". 请参阅 time 模块中的文档了解如 何记录用户上次登录的时间. 另外提供一个"系统管理员", 它可以导出所有用户的用户名, 密码 (如果想要的话，你可以把密码加密), 以及"上次登录时间".

** a) 数 据 应 该 保 存 在 磁 盘 中 , 使 用 冒 号 ( : ) 分 割 , 一 次 写 入 一 行 , 例 如 "joe: boohoo: 953176591.145", 文件中数据的行数应该等于你系统上的用户数. **

** b) 进一步改进你的程序, 不再一次写入一行, 而使用 pickle 模块保存整个数据对象. 请参 阅 pickle 模块的文档了解如何序列化/扁平化对象, 以及如何读写保存的对象. 一般来说, 这个 解决方案的代码行数要比a) 的少. **

**　c) 使用 shelve 模块替换 pickle 模块, 由于可以省去一些维护代码，这个解决方案的代码比 b) 的更少 **
	#!/usr/bin/env python

	from datetime import datetime
	import hashlib, os
	import pickle as p
	import shelve as s
	
	db = {}
	
	def newuser():
	    value = []
	    prompt = 'login name desired again: '
	    while True:
	        name = raw_input(prompt).lower()
	        if not name.isalnum() and '' in name:
	            print 'name format error'
	            continue
	        else:
	            break
	    pwd = raw_input('login passwd desired: ')
	    m = hashlib.md5()
	    m.update(pwd)
	    value.append(m.hexdigest())
	    value.append(datetime.now())
	    db[name] = value
	    print 'new user is %s, register time is %s' % (name, db[name][1])
	
	def olduser():
	    name = raw_input('login name desired again: ').lower()
	    pwd = raw_input('login passwd desired: ')
	    m = hashlib.md5()
	    m.update(pwd)
	    passwd = db.get(name)
	    if passwd[0] == m.hexdigest():
	        newtime = datetime.now()
	        if (newtime - db[name][1]).days == 0 and (newtime - db[name][1]).seconds < 14400:
	            print 'you already logged in at %s' %(db[name][1])
	        else:
	            passwd[1] = newtime
	            print 'welcome back %s, login time is %s' %(name, passwd[1])
	    else:
	        print 'login incorrect'
	
	def removeuser():
	    print db
	    name = raw_input('input a user name to remove: ').lower()
	    if name in db:
	        db.pop(name)
	    else:
	        print 'input error'
	
	def userlogin():
	    while True:
	        name = raw_input('login name desired: ').lower()
	        if not name.isalnum() and '' in name:
	            print 'name format error'
	            continue
	        else:
	            if not db.has_key(name):
	                print 'user name is not in db'
	                answer = raw_input('register a new user? y/n').lower()
	                if 'y' == answer:
	                    newuser()
	                elif 'n' == answer:
	                    break;
	            else:
	                print 'user name is already in db'
	                olduser()
	                break
	
	def output_use_file():
	    print db
	    f = open('account.txt', 'w')
	    for key in db:
	        user = key + ':' + db[key][0] + ':' + str(db[key][1]) + os.linesep
	        f.write(user)
	    f.close()
	
	def output_use_pickle():
	    accountfile = 'pickle.data'
	    f = open(accountfile, 'w')
	    p.dump(db, f)
	    f.close()
	
	    f = open(accountfile)
	    accountdb = p.load(f)
	    print accountdb
	
	def output_use_shelve():
	    accountfile = 'shelve.data'
	    accountdb = s.open(accountfile, 'c')
	    accountdb['data'] = db
	    accountdb.close()
	
	    accountdb = s.open(accountfile, 'r')
	    print accountdb['data']
	
	def adminlogin():
	    while True:
	        name = raw_input('login name desired: ').lower()
	        if not name.isalnum() and '' in name:
	            print 'name format error'
	            continue
	        else:
	            pwd = raw_input('login passwd desired: ')
	            if name == 'root' and pwd == 'root':
	                print 'welcome admin'
	                break
	            else:
	                print 'user name or passwd is wrong, input again'
	    if len(db) == 0:
	        print 'there is nothing you can do'
	    else:
	        answer = raw_input('output all account? y/n').lower()
	        if 'y' == answer:
	            #output_use_file()
	            #output_use_shelve()
	            output_use_pickle()
	        elif 'n' == answer:
	            print 'bye'
	
	def showmenu():
	    prompt = """
	     (A)dmin Login
	     (U)ser Login
	     (R)emove a existing user
	     (Q)uit
	     Enter choice:"""
	
	    done = False
	    while not done:
	        chosen = False
	        while not chosen:
	            try:
	                choice = raw_input(prompt).strip()[0].lower()
	            except (EOFError, KeyboardInterrupt):
	                choice = 'q'
	            print '\nYou picked:[%s]' %choice
	            if choice not in 'aurq':
	                print 'invalid option, try again'
	            else:
	                chosen = True
	
	        if choice == 'q':
	            done = True
	        elif choice == 'r':
	            removeuser()
	        elif choice == 'u':
	            userlogin()
	        elif choice == 'a':
	            adminlogin()
	
	if __name__ == '__main__':
	    showmenu()
	
####9.13. 命令行参数 a) 什么是命令行参数, 它们有什么用? b) 写一个程序, 打印出所有的命令行参数.

    import sys
	print str(sys.argv)

####9.14. 记录结果. 修改你的计算器程序(练习 5-6 )使之接受命令行参数. 略。

####9–15. 复制文件. 提示输入两个文件名(或者使用命令行参数). 把第一个文件的内容复制到第二个文件中去.

	#!/usr/bin/env python

	def copyfile(src, dst):
	    with open(dst, 'a') as f:
	        with open(src) as s:
	            for item in s:
	                f.write(item)
	
	if __name__ == '__main__':
	    src = raw_input('copy from: ')
	    dst = raw_input('copy to: ')
	    copyfile(src, dst)

####9.16. 文本处理. 人们输入的文字常常超过屏幕的最大宽度. 编写一个程序, 在一个文本文件中查找长度大于 80 个字符的文本行. 从最接近 80 个字符的单词断行, 把剩余文件插入到 下一行处.

略。

####**9.17. 文本处理. 创建一个原始的文本文件编辑器. 你的程序应该是菜单驱动的, 有如下这些选项: **

创建文件(提示输入文件名和任意行的文本输入),
显示文件(把文件的内容显示到屏幕),
编辑文件(提示输入要修改的行, 然后让用户进行修改),
保存文件,
退出.
略。

####9.18. 搜索文件. 提示输入一个字节值(0 - 255)和一个文件名. 显示该字符在文件中出现的次数.
	#!/usr/bin/env python

	def counts(filename, value):
	    ch = chr(value)
	    with open(filename, 'rb') as f:
	        total = sum(item.count(ch) for item in f)
	    return total
	
	if __name__ == '__main__':
	    filename = raw_input('file name:')
	    value = int(raw_input('value: '))
	    print counts(filename, value)

#### 9–19. 创建文件. 创建前一个问题的辅助程序. 创建一个随机字节的二进制数据文件, 但某一特定字节会在文件中出现指定的次数. 该程序接受三个参数:

一个字节值( 0 - 255 ),
该字符在数据文件中出现的次数, 以及
数据文件的总字节长度. 你的工作就是生成这个文件, 把给定的字节随机散布在文件里, 并且要求保证给定字符在文件中只出现指定的次数, 文件应精确地达到要求的长度.

	#!/usr/bin/env python

	from random import randint
	
	def create(filenmae, value, total, maxlen):
	    assert 0 <= value <= 255
	    ls = [chr(randint(0, 255)) for i in xrange(maxlen - total)]
	    ch = chr(value)
	    for i in xrange(total - ls.count(ch)):
	        ls.insert(randint(0, len(ls) - 1), ch)
	    for i in xrange(maxlen - len(ls)):
	        ls.insert(randint(0, len(ls)-1), chr(randint(0, value - 1)))
	    with open(filename, 'wb') as f:
	        f.write(''.join(ls))
	
	if __name__ == '__main__':
	    filename = raw_input('filename: ')
	    value = int(raw_input('value: '))
	    total = int(raw_input('total: '))
	    maxlen = int(raw_input('max length of file: '))
	    create(filename, value, total, maxlen)
	
####9.20 压缩文件. 写一小段代码, 压缩/解压缩 gzip 或 bzip 格式的文件. 可以使用命令行下的 gzip 或 bzip2 以及 GUI 程序 PowerArchiver , StuffIt , 或 WinZip 来确认你的 Python支持这两个库.

	#!/usr/bin/env python

	import gzip
	
	def compress(zipfile, filename):
	    obj = gzip.open(zipfile, 'wb')
	    with open(filename, 'rb') as f:
	        obj.writelines(f)
	    obj.close()
	
	def decompress(zipfile, filename):
	    obj = gzip.open(zipfile, 'rb')
	    content = obj.read()
	    with open(filename, 'wb') as f:
	        f.write(content)
	
	if __name__ == '__main__':
	    compress('compress.gzip', 'test.txt')
	    decompress('compress.gzip', 'decompress.txt')

#### 9.21. ZIP 归档文件. 创建一个程序, 可以往 ZIP 归档文件加入文件, 或从中提取文件,有可能的话, 加入创建ZIP 归档文件的功能

	#!/usr/bin/env python

	import zipfile
	
	def create_zipfile(zipname, filename1, filename2):
	    z = zipfile.ZipFile(zipname, 'w')
	    z.write(filename1)
	    z.write(filename2)
	    z.close()
	
	def add_zipfile(zipname, filename):
	    z = zipfile.ZipFile(zipname, 'a')
	    z.write(filename)
	    z.close()
	
	def extract_zipfile(zipname, filename):
	    z = zipfile.ZipFile(zipname, 'r')
	    z.extract(filename)
	    z.close()
	
	def zipfile_filelist(zipname):
	    z = zipfile.ZipFile(r'test.zip', 'r')
	    z.printdir()
	    z.close()
	
	if __name__ == '__main__':
	    create_zipfile(r'test.zip', r'test.txt', r'test1.txt')
	    add_zipfile(r'test.zip', r'test2.txt')
	    extract_zipfile(r'test.zip', r'test1.txt')
	    zipfile_filelist(r'test.zip')
	
#### 9.22  ZIP 归档文件. unzip -l 命令显示出的 ZIP 归档文件很无趣. 创建一个 Python 脚本 lszip.py , 使它可以显示额外信息: 压缩文件大小, 每个文件的压缩比率(通过比较压缩 前后文件大小), 以及完成的 time.ctime() 时间戳, 而不是只有日期和 HH:MM . 提示: 归档文件的 date_time 属性并不完整, 无法提供给 time.mktime() 使用....这由你自己决定.
	#!/usr/bin/env python
	
	import zipfile, os, time
	
	filename = raw_input('zip file name:')
	print 'zip file size:%d bytes' % (os.stat(filename).st_size)
	
	z = zipfile.ZipFile(filename, 'r')
	print 'filename\tdatetime\tsize\tcompress size\trate'
	for info in z.infolist():
	    t = time.ctime(time.mktime(tuple(list(info.date_time)+[0,0,0])))
	    print '%s\t%s\t%d\t%d\t%.2f%%' %(
	    info.filename, t, info.file_size, info.compress_size, float(info.compress_size) / info.file_size *100)
	
	z.close()
	
#### 9.23 TAR 归档文件. 为 TAR 归档文件建立类似上个问题的程序. 这两种文件的不同之处在于 ZIP 文件通常是压缩的, 而 TAR 文件不是, 只是在 gzip 和 bzip2 的支持下才能完成压缩工作. 加入任意一种压缩格式支持.附加题: 同时支持 gzip 和 bzip2 .

	#!/usr/bin/env python
	
	import tarfile
	
	def create_tarfile(tarname, filename1, filename2):
	    t = tarfile.open(tarname, 'w:gz')
	    t.add(filename1)
	    t.add(filename2)
	    t.close()
	
	def extract_tarfile(tarname, des_dir):
	    t = tarfile.open(tarname, 'r')
	    t.extractall(des_dir)
	    t.close()
	
	if __name__ == '__main__':
	    create_tarfile(r'test.tar.gz', r'test.txt', r'test1.txt')
	    extract_tarfile(r'test.tar.gz', r'extract_tarfile')

#### 9.24 归档文件转换.参考前两个问题的解决方案, 写一个程序, 在 ZIP (.zip) 和TAR/gzip (.tgz/.tar.gz) 或 TAR/bzip2 (.tbz/.tar.bz2) 归档文件间移动文件. 文件可能是已经存在的, 必要时请创建文件.

	#!/usr/bin/env python
	
	import tarfile
	import zipfile
	import os
	
	def movefile(src, dst, filename):
	    if src.endswith('.zip') and dst.endswith(('.tar.gz', '.tgz', '.tbz', '.tar.b                                                                                        z2')):
	        zipobj = zipfile.ZipFile(src, 'r')
	        content = zipobj.read(filename)
	        zipobj.close()
	
	        with open(filename, 'w') as f:
	            f.write(content)
	
	        tar = tarfile.open(dst, 'r')
	        ls = tar.getnames()
	        tar.extractall()
	        tar.close
	
	        mode = 'w:gz' if dst.endswith(('tar.gz', '.tgz')) else 'w:bz2'
	        tar = tarfile.open(dst, mode)
	        for name in ls + [filename]:
	            tar.add(name)
	            os.remove(name)
	        tar.close()
	    elif src.endswith(('.tar.gz', '.tgz', '.tbz', '.tar.bz2')) and dst.endswith(                                                                                        '.zip'):
	        tar = tarfile.open(src, 'r')
	        tar.extract(filename)
	        tar.close()
	
	        zipobj = zipfile.ZipFile(dst, 'a')
	        zipobj.write(filename)
	        zipobj.close()
	        os.remove(filename)
	
	if __name__ == '__main__':
	    movefile(r'test.zip', r'test2.tar.gz', r'test2.txt')
	    movefile(r'test2.tar.gz', r'test.zip', r'test2.txt')

#### 9.25  通用解压程序. 创建一个程序, 接受任意数目的归档文件以及一个目标目录做为参数. 归档文件格式可以是 .zip, .tgz, .tar.gz, .gz, .bz2, .tar.bz2, .tbz 中的一种或几种. 程序会把第一个归档文件解压后放入目标目录, 把其它归档文件解压后放入以对应文件名命名的目录下 (不包括扩展名). 例如输入的文件名为 header.txt.gz 和 data.tgz ，目录为 incoming , header.txt 会被解压到 incoming 而 data.tgz 中的文件会被放入 incoming/data 

	

	
	
	
