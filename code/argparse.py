import argparse


def get_args():
    parser = argparse.ArgumentParser("Genshin Auto Domain")
    parser.add_argument("--yolox_exp_file", type=str, default='yolox/exp/yolox_s_genshin.py')
    parser.add_argument("--lost_score", type=float, default=0.6)
    parser.add_argument("--lost_times", type=int, default=4)
    parser.add_argument("--track_timeout", type=float, default=4.5)
    parser.add_argument("--max_retry", type=int, default=200)
    return parser.parse_args()


args = get_args()
print(args.max_retry)
