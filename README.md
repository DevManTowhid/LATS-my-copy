# LATS Model Workflow

The following describes the complete workflow for the **LATS model**, likely referring to a model for **summarization** or **natural language generation**. 

### 1. **Unlabeled Document Data:**

The workflow begins with the collection of **unlabeled document data** from various sources, such as:

- **C4**: A large dataset for text-based tasks (like summarization) commonly used in NLP research.
- **HugeNews**: Another dataset or source of news data.
- **CNN** and **Daily Mail**: Well-known datasets used for news summarization tasks.

### 2. **Corpus Sample:**

From these diverse data sources, a **Corpus Sample** is created, containing a mix of unstructured document data that will be used for the training process.

### 3. **Pre-training (GSG Task - PEGASUS):**

- **Pre-training Step**: The **PEGASUS model** is pre-trained on this corpus. The pre-training task is referred to as **GSG (Generative Summarization Goal)**. This task teaches the model to generate summaries by learning from large corpora of text and summaries, enabling it to generalize better for downstream tasks.
- **Output**: This produces a **pre-trained model** that can be fine-tuned for various text generation tasks.

### 4. **Easy Data Augmentation:**

Data augmentation techniques are applied to the corpus. This could involve techniques such as:

- **Synonym replacement**.
- **Random insertions**.
- **Random deletions**.
- **Sentence shuffling**, etc.

#### **Goal**: This step aims to enrich the corpus by creating augmented versions of the original corpus, which helps improve the model’s ability to generalize.

### 5. **Augmented Corpus Sample:**

After data augmentation, the **Augmented Corpus Sample** is ready for the next phase. This sample includes both the original and the augmented data and will be used for fine-tuning and training.

### 6. **Compute Edit Distance Task:**

- **Edit Distance**: This task calculates the **edit distance** between different versions of the document and its summary (e.g., between the article and the generated summary). The edit distance measures how many operations (insertions, deletions, substitutions) are required to transform one text into another.
- **Purpose**: Helps the model evaluate the quality of summaries in terms of how much editing is needed to match a reference summary.

### 7. **Operation Values:**

In this step, various **operation values** are calculated based on the edit distance. These values quantify different operations like:

- **Insertions**: Additional words added in the summary.
- **Deletions**: Words removed from the summary.
- **Substitutions**: Words substituted in the summary.

These values are then used to assess the quality and accuracy of the generated summaries.

### 8. **Training Data Curriculum:**

The training process is organized as a **curriculum**, starting with simpler data samples and gradually increasing the complexity of the samples the model is exposed to. The goal is to improve the model's training efficiency and effectiveness by carefully structuring the training data.

### 9. **Sorting Task:**

The data is sorted according to certain criteria, such as **complexity**, which could depend on factors like sentence length, semantic difficulty, or ambiguity.

#### **Purpose**: Sorting the data allows the model to train progressively, improving its performance on more challenging tasks as it progresses through the curriculum.

### 10. **Complexity Score:**

A **complexity score** is assigned to each training example. This score reflects the difficulty of the example for the model to process. Examples could be based on the length of the text, the difficulty of summarizing, or other factors like syntactic or semantic complexity.

#### **Role**: These scores help to prioritize which data should be introduced at different stages of training.

### 11. **Operation Hyperparameter Selection Task:**

This task fine-tunes various **hyperparameters** for the operations (such as edit distance metrics and complexity scoring), ensuring optimal training performance.

#### **Goal**: The task aims to select hyperparameters that maximize the performance of the model in the context of the summarization task.

### 12. **Downstream Training Task (PEGASUS):**

The **pre-trained PEGASUS model** is now fine-tuned using the augmented, sorted, and properly ranked data. This step involves training the model to generate high-quality summaries based on the dataset and curriculum.

#### **Output**: This produces the fine-tuned **PEGASUS model**, which is ready for application in summarization tasks.

### 13. **LATS Model:**

The output of the downstream training task is the **LATS model**, which stands for a **Layered Approach to Text Summarization**. This model has been trained with curriculum learning and can generate summaries with improved quality, coherence, and readability.

---

## Key Concepts in the Diagram:

- **Pre-training and Fine-Tuning**: The model begins with pre-training on a general corpus, followed by fine-tuning on a more specific dataset.
- **Curriculum Learning**: The data is sorted by complexity, with easier examples presented first, gradually progressing to harder ones.
- **Data Augmentation**: Techniques like synonym replacement and sentence shuffling are used to augment the dataset and improve model generalization.
- **Evaluation Tasks**: Metrics like edit distance are used to evaluate the quality of the summaries generated by the model.
