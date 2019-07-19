cd crawler
rm -fr dist
mkdir dist
# pip install -r requirements.txt -t dist
cp src/*.py dist
cd dist
docker run -v $(pwd):/outputs -it --rm lambci/lambda:build-python3.6 pip install scrapy -t /outputs/
# zip -r deploy.zip *
cd ../..
terraform apply -lock=true -auto-approve