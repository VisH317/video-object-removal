import os
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from pydantic import BaseModel

import argparse
from mask import mask
from inpaint import inpaint

app = FastAPI()

class Item(BaseModel):
    file: UploadFile = File()
    x: int
    y: int
    w: int
    h: int


@app.post("/inpaint")
async def inpaint(item: Item):
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
    return FileResponse('./results/inpainting/vid.mp4')
    # write into a file or find a way to send the direct stream data
    # setup the arguments and run mask and paint, get the returned file and send raw