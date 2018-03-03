for filename in *
do
    echo $filename
    markdown-pdf $filename
done;
