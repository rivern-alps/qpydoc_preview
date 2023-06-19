chcp 65001
@echo off

set opt=%1
set ret=0
set project_root=%CD%

set css_dest_dir=%project_root%\out\doc\static\css\theme_default
set js_dest_dir=%project_root%\out\doc\static\js\theme_default
set css_src_dir=%project_root%\static\css\theme_default
set js_src_dir=%project_root%\static\js\theme_default

teedoc build

if not exist %css_src_dir% (
	echo !!!!teedoc 编译失败!!!!
	set ret=1
	goto exit
) else (
	xcopy /y %css_src_dir%\light.css %css_dest_dir%\
	xcopy /y %js_src_dir%\main.js %js_dest_dir%\
)


if /i "%opt%"=="-s" (
	echo 本地预览地址: http://127.0.0.1:8000/doc/
	echo 退出预览模式: Ctrl + C
	call python.exe -m http.server 8000 -d out/
) else (
	echo 编译完成,输出文件目录: out\
)

:exit
exit /B %ret%