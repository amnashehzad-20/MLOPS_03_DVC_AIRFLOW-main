# News Data Pipeline

A data engineering pipeline that collects news data from the News API, processes it, and trains a machine learning model, with versioning using DVC and workflow automation using Airflow.

## Project Structure

```
NewsDataPipeline/
│
├── data/                 # Directory for data storage
│   ├── raw_data.csv     # Raw data collected from News API
│   └── processed_data.csv # Preprocessed data
│
├── dags/                 # Airflow DAGs
│   └── news_pipeline_dag.py # Main pipeline DAG
│
├── models/               # Directory for storing trained models
│   └── model.pkl        # Trained linear regression model
│
├── scripts/              # Python scripts for the pipeline
│   ├── collect_data.py  # Script for collecting data from News API
│   ├── preprocess_data.py # Script for preprocessing data
│   └── train_model.py   # Script for training the model
│
├── .env                  # Environment variables (API keys)
├── .gitignore            # Git ignore file
├── dvc.yaml              # DVC pipeline definition
├── metrics.json          # Metrics file for DVC
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

## Setup Instructions

1. Clone the repository
2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up your News API key in the `.env` file:
   ```
   NEWS_API_KEY=your_news_api_key_here
   ```
4. Initialize Git and DVC:
   ```
   git init
   dvc init
   ```
5. Set up a DVC remote:
   ```
   dvc remote add -d myremote /path/to/remote/storage
   ```
6. Start Airflow:
   ```
   airflow standalone
   ```

## Running the Pipeline

### Using DVC

To run the entire pipeline with DVC:
```
dvc repro
```

To run individual stages:
```
dvc repro collect_data
dvc repro preprocess_data
dvc repro train_model
```

### Using Airflow

The DAG is scheduled to run daily. You can also trigger it manually from the Airflow UI.

## Data Versioning with DVC

Track changes to data files:
```
dvc add data/raw_data.csv
dvc add data/processed_data.csv
```

Track changes to the model:
```
dvc add models/model.pkl
```

Push to DVC remote:
```
dvc push
```

Pull from DVC remote:
```
dvc pull
```

## Pipeline Steps

1. **Data Collection**: Fetches news articles from the News API
2. **Data Preprocessing**: Cleans and normalizes the data
3. **Model Training**: Trains a linear regression model to predict content length

## Metrics

Model performance metrics are stored in `metrics.json` and tracked by DVC.
