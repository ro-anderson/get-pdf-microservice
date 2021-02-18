# Invoice Digitizer

# build image
docker build -t nrn-invoice-digitizer .

# run container
docker run --name nrn-invoice-digitizer -p 127.0.0.1:5000:5000 nrn-invoice-digitizer
