# commentTitle

**Add a big Title to the file**

2015/10/25 by DKZ update 2016/1/14


Make a new file with comment title like this

```
=================================================================================================
                                                               ________                          
                                                        _     |__    __| __  _      __           
 ______    _____   ___  ___  ___  ___   _____  ______  | \_      |  |   |__|| \_   |  |    _____ 
|   ___|  /     \ |   \/   ||   \/   | /  _  \|      \ |   _|    |  |   |  ||   _| |  |   /  _  \
|  |____ |   o   ||        ||        |/  ____/|   _   ||  |___   |  |   |  ||  |___|  |_ /  ____/
|_______| \_____/ |__|\/|__||__|\/|__|\______/|__| |__|\_____/   |__|   |__|\_____/|____|\______/
=================================================================================================
```

And add license(MIT,BSD,GPL,LGPL,apache) in the head


	                           All linked works must    _Y_ GPL
	                           be issued under the     |
	                       _Y_ same or compatible   ---| 
	                      |    license                 |_N_ LGPL
	                      |
	Modified versions     |
	must be issued under--|   Every file must             _Y_ Apache
	the same license      |   contain all information    |
	                      |   about changes, copyrights  | 
	                      |_N_and patents.             --|         
	                          Patent protection          |                        _Y_ BSD
 	                                                     |   Prohibit use of     |
	                                                     |_N_copyright holder's--|
	                                                         name for promotion  |_N_ MIT
	                                                         
	                                       <How to select Licenses>       2016/4/29 by DKZ


### Usage
```
$python commentTitle.py
file name:
test.py
...

$python commentTitle.py filename.py -t title -a author -c contact -l license -d desc
```

### windows command

PATH + commentTitle.py's path

PATHEXT + ;.py


### linux terminal

.bashrc +

    alias commentTitle="python3 commentTitlepy_Path/commentTitle.py"
