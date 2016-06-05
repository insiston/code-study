#!/bin/bash
#Author: vforbox
#Script_file : generate_album.sh

echo "Createing album....."

cat <<EOF1 > index.html

<html>
<head>
<style>

body
{
        width:470px;
        margin:auto;
        border: 1px dashed grey;
        padding:10px;
}

img
{
        margin:5px;
        border: 1px solid black;

}
</style>
</head>
<body>
<center><h1> #Album title </h1></center>
<p>
EOF1
read -p "Please enter a img storage path: " Path
for img in $Path;
do
        convert "$img" -resize "100x" "$img"
        echo "<a href=\"$img\" ><img src=\"$img\" title=\"$img\" /></a>" >> index.html
done

cat <<EOF2 >> index.html

</p>
</body>
</html>
EOF2
echo Album generated to index.html
