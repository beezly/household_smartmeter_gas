docker build -t build_$$ .
docker tag build_$$ ghcr.io/beezly/household_smartmeter_gas:latest
docker push ghcr.io/beezly/household_smartmeter_gas:latest
