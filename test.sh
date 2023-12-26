python trainer.py --lr=0.1 --momentum=0.9 --nesterov --batch-size=512 --world_size=16 --graph=ring --neighbors=2 --arch=vgg11 --alpha=0.01 --epochs=300 --gamma=0.09 --growth_rate=1.01 --seed=1234 
cd ./outputs
python dict_to_csv.py --arch=vgg11 --world_size=16 --graph=ring --gamma=0.09 --alpha=0.01 --seed=1234
cd ..

python trainer.py --lr=0.1 --momentum=0.9 --nesterov --batch-size=512 --world_size=16 --graph=ring --neighbors=2 --arch=resnet --alpha=0.01 --epochs=300 --gamma=0.09 --growth_rate=1.01 --seed=1234 
cd ./outputs
python dict_to_csv.py --arch=resnet --world_size=16 --graph=ring --gamma=0.09 --alpha=0.01 --seed=123
cd ..


