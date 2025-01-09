---
title: Deployment Model Inference
description: A description of the project.
---

# Deployment Model Inference

This project demonstrates a Dockerized inference pipeline for deploying a machine learning model. The pipeline loads a trained model, preprocesses input data, and makes predictions using the model.

## Table of Contents
- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Docker Deployment](#docker-deployment)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

The project consists of the following components:
- **`src/inference.py`**: The main script that loads the model, preprocesses input data, and makes predictions.
- **`src/model_loader.py`**: A utility script to load the trained model.
- **`src/data_preprocessor.py`**: A utility script to preprocess input data.
- **`models/trained_model_2025-01-02.joblib`**: A trained model saved in the `models/` directory.
- **`Dockerfile`**: A Dockerfile to containerize the inference pipeline.
- **`pyproject.toml`**: A Poetry configuration file for dependency management.

---

## Prerequisites

Before running the project, ensure you have the following installed:
- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/iair/deployment_model_inference.git
   cd deployment_model_inference
   ```

2. Install dependencies using pip:
   ```bash
   pip install requirements.txt
   ```

---

## Usage

### Running Locally
1. Run the inference script:
   ```bash
   uvicorn main:app --port 4579 --reload
   ```

### Input Data
The script expects input data in the following format:
```python
input_data = {
    "Education": 1,
    "Income": 49854.0,
    "Kidhome": 1,
    "Teenhome": 0,
    "Recency": 63,
    "Wines": 123,
    "Fruits": 17,
    "Meat": 171,
    "Fish": 39,
    "Sweets": 0,
    "Gold": 0,
    "NumDealsPurchases": 0,
    "NumWebPurchases": 0,
    "NumCatalogPurchases": 0,
    "NumStorePurchases": 0,
    "NumWebVisitsMonth": 0,
    "AcceptedCmp3": 0,
    "AcceptedCmp4": 0,
    "AcceptedCmp5": 0,
    "AcceptedCmp1": 0,
    "AcceptedCmp2": 0,
    "Complain": 0,
    "Response": 0,
    "Edad": 42,
    "En_Convivenvia": 1,
    "Hijos": 1,
    "Tamanho_familiar": 3,
    "Es_Padre": 1,
    "Clusters": 3,
    "Total_Promos": 0
}
```

---

## Docker Deployment

### Build the Docker Image
To build the Docker image, run:
```bash
docker build -t inference-service-6 .
```

### Run the Docker Container
To run the container and execute the inference script:
```bash
docker run -d -p 4579:8080 --name inference-service-container inference-service-6

```

### Mount Local Files (Optional)
If you want to test changes to your code or model without rebuilding the Docker image, mount your local project directory into the container:
```bash
docker run -it -v $(pwd):/app deployment_model_inference:latest
```

---

## Testing

To test the inference pipeline, ensure the model file (`models/trained_model_2025-01-02.joblib`) exists and is correctly loaded. You can also test with different input data to verify the pipeline's robustness.

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## License

This project is licensed under the **Apache 2.0 License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Thanks to the open-source community for providing tools and libraries that made this project possible.
- Special thanks to [Poetry](https://python-poetry.org/) and [Docker](https://www.docker.com/) for simplifying dependency management and deployment.

---

## Contact

For questions or feedback, feel free to reach out:
- **Author**: Iair
- **Email**: i.linker8@gmail.com
- **GitHub**: [iair](https://github.com/iair)


---

### **How to Use**
1. Open your project in Visual Studio Code.
2. Open the `README.md` file (or create one if it doesn’t exist).
3. Copy and paste the above content into the file.
4. Save the file (`Ctrl + S` or `Cmd + S`).

---
