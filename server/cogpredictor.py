from cog import BasePredictor, File, Input
import argparse
import os

from mask import mask
from inpaint import inpaint

class Predictor(BasePredictor):
    def setup(self):
        pass

    def predict(self, video: File = Input(description="video"), x: int = Input(description='coordinate'), 
    y: int = Input(description='coordinate'), 
    w: int = Input(description='coordinate'), 
    h: int = Input(description='coordinate')) -> File:
        os.remove('./results/inpainting/vid.mp4')
        parser = argparse.ArgumentParser()
        parser.add_argument('--data')
        parser.add_argument('--x')
        parser.add_argument('--y')
        parser.add_argument('--w')
        parser.add_argument('--h')
        parser.add_argument('--resume')
        parser.add_argument('--mask-dilation')
        parser.add_argument('--name')
        arglist = ['--data', item.file, '--x', item.x, '--y', item.y, '--w', item.w, '--h', item.h, '--resume', 'cp/SiamMask_DAVIS.pth', '--mask-dilation', 32, '--name', 'vid']
        args = parser.parse_args([arglist])

        mask(args)
        inpaint(args)
        return File('./results/inpainting/vid.mp4')
