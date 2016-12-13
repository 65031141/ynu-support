watchmedo shell-command \
    --patterns="*.py;*.md" \
    --recursive \
    --command='echo "File ${watch_src_path} changed and now regenerate html" && make html' &

livereload output &
