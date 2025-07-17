# 🧱 3D Reconstruction on Raspberry Pi 4 (Structure from Motion)

This project demonstrates how to perform **complete 3D reconstruction** from images captured using a **single Pi Camera V2** on a **Raspberry Pi 4**. The entire pipeline, from image capture to dense 3D model generation, runs locally on the Pi using lightweight SfM tools.

---

## 📸 Features

- Use **Raspberry Pi Camera V2** to capture image sequences
- Perform full **Structure from Motion** (SfM) on Raspberry Pi 4
- Generate **sparse and dense point clouds**, meshes, and textured models
- Tools used: `picamera2`, **OpenMVG**, and **OpenMVS`
- Lightweight and optimized for low-resource devices

---

## 🖥️ Hardware Requirements

- ✅ Raspberry Pi 4 (4 GB or 8 GB recommended)
- ✅ Pi Camera V2 (configured and enabled)
- ✅ Heatsink/fan (recommended for long computations)
- ✅ 16 GB+ SD card
- ✅ (Optional) Active cooling or swap memory enabled

---

## 🧰 Software Stack

| Component       | Purpose                      |
|----------------|------------------------------|
| Picamera2      | Image capture from PiCam     |
| OpenCV         | Image resizing/compression   |
| OpenMVG        | Feature extraction + SfM     |
| OpenMVS        | Dense point cloud, mesh, texture |
| MeshLab/Blender| Visualization (on PC)        |

---

## 🚀 Setup Instructions

### 📦 1. Install Dependencies

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-picamera2 python3-opencv \
    build-essential git cmake libjpeg-dev libpng-dev libtiff-dev \
    libboost-all-dev libeigen3-dev libflann-dev libopencv-dev
