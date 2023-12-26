import torch
import csv
import os
import argparse
parser = argparse.ArgumentParser(description='Propert ResNets for CIFAR10 in pytorch')
parser.add_argument('--save-dir', dest='save_dir',
                    help='The directory used to save the trained models',
                    default=None, type=str)
parser.add_argument('--output-file', dest='output_file',
                    help='The directory used to save the trained models',
                    default='output.tsv', type=str)

parser.add_argument('--arch', dest='arch',help='Architecture of model',default="resnet", type=str)
parser.add_argument('-world_size', '--world_size', default=16, type=int, help='total number of nodes')
parser.add_argument('--graph', '-g',  default='ring', help = 'graph structure - [ring, torus]' )
parser.add_argument('--gamma', help='The directory used to save the trained models',default=1.0, type=float)
parser.add_argument('--alpha',  default=1.0, type=float, help='NGC mixing weight')
parser.add_argument('--seed', default=1234, type=int,   help='set seed')


args = parser.parse_args()

if args.save_dir is None:
    args.save_dir = args.arch+"_"+args.graph+"_nodes"+str(args.world_size)+"_alpha_"+str(args.alpha)+"_gamma_"+ str(args.gamma)+"_seed_"+str(args.seed)
    
else:
    args.save_dir += args.arch+"_"+args.graph+"_nodes"+str(args.world_size)+"_alpha_"+str(args.alpha)+"_gamma_"+ str(args.gamma)+"_seed_"+str(args.seed)
 
def average(input):
    return sum(input)/len(input)
dict_data = torch.load(os.path.join(args.save_dir, "excel_data","dict"))
fields = dict_data.keys()
dict_data["avg test acc"] = average(dict_data["avg test acc"])
dict_data["avg test acc final"] = average(dict_data["avg test acc final"])
dict_data["data transferred"] = average(dict_data["data transferred"])

if not( os.path.isfile(args.output_file) ):
    with open(args.output_file, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames= fields, delimiter='\t' )
        writer.writeheader()


with open(args.output_file, 'a') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames= fields, delimiter='\t' )
    writer.writerow(dict_data)