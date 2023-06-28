#!bin/bash
echo "Enter commit message:"
read commit_message

if [ -z $commit_message ]; then
    commit_message='.'
fi
git add .
git commit -m "$commit_message"
git push
