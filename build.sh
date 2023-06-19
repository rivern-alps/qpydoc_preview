# !/bin/bash

css_dest_dir="out/doc/static/css/theme_default/"
js_dest_dir="out/doc/static/js/theme_default/"
css_src_dir="static/css/theme_default/"
js_src_dir="static/js/theme_default/"
teedoc build
if [ ! -d ${css_src_dir} ]; then
	# mkdir -p ${css_src_dir}
	echo "teedoc 编译失败"
else
cp -R ${css_src_dir}/light.css ${css_dest_dir}/light.css
cp -R ${js_src_dir}/main.js ${js_dest_dir}/main.js
fi

# if [ ! -d ${js_src_dir} ]; then
	# cp
# fi


if [ $# == 0 ];then
	echo "编译完成,输出文件目录: out/";
else
	if [ $1 = "-s" ]; then
		echo "本地预览地址: http://127.0.0.1:8000/doc/"
		echo "退出预览模式: Ctrl + C"
		python -m http.server 8000 -d out/
	fi
fi
