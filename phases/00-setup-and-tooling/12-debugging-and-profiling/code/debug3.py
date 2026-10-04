import logging
import torch
from time import sleep

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("training.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

lr=0.01; batch_size=64
loss=119.71839123; step=11
nan_step=25

sleep(3)
logger.info("Starting training: lr=%.4f, batch_size=%d", lr, batch_size)

sleep(5)
logger.warning("Loss spike detected: %.4f at step %d", loss, step)

sleep(5)
logger.error("NaN loss at step %d, stopping", step)