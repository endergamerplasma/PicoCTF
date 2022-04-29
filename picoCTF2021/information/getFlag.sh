encodedFlag="$(exiftool cat.jpg | grep License.*)"
encodedFlag=${encodedFlag##*:}
echo $encodedFlag | base64 -d
echo
