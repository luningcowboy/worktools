cd assets
files=$(svn st | grep ? | sed 's/\?//g' | sed 's/ //g')
for i in $files; do
	svn add $i
done
