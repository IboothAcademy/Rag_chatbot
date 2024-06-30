# What is a Large Language Model (LLM)?

A Large Language Model (LLM) is a type of artificial intelligence (AI) program capable of tasks such as recognizing and generating text. The name "large" refers to the vast datasets these models are trained on. LLMs are based on machine learning, specifically a type of neural network called a transformer model.

In simple terms, an LLM is a computer program that has been given enough examples to recognize and interpret human language or other complex data. Many LLMs are trained on thousands or even millions of gigabytes of text collected from the internet. However, the quality of the samples impacts how well an LLM can learn natural language, so programmers may use more curated datasets.

LLMs use a type of machine learning called deep learning to understand how letters, words, and sentences work together. Deep learning involves probabilistic analysis of unstructured data, allowing the model to recognize distinctions between content without human intervention.

Further learning is achieved through tuning. LLMs are fine-tuned or prompt-adjusted for specific tasks that programmers desire, such as interpreting questions, generating responses, or translating text from one language to another.

### Use Cases for LLMs

LLMs can be trained for a variety of tasks. One well-known application is as generative AI, which can produce text in response to a given prompt or question. For example, the publicly available LLM ChatGPT can generate essays, poems, and other forms of text based on user input.

Any large and complex dataset, including programming languages, can be used to train an LLM. Some LLMs can assist programmers in writing code, generating functions on request, or completing a program when given a starting point. LLMs can also be used for:

- Sentiment analysis
- DNA research
- Customer service
- Chatbots
- Online searches

Examples of real LLMs include ChatGPT (by OpenAI), Bard (by Google), Llama (by Meta), and Bing Chat (by Microsoft). GitHub Copilot is another example, although it is designed for coding rather than natural human language.

### Advantages and Limitations of LLMs

The primary feature of an LLM is its ability to respond to unpredictable queries. Traditional computer programs respond to commands given in permitted syntax or specific user inputs. Video games have limited buttons, applications have restricted items to click or input, and programming languages consist of precise if/then statements.

In contrast, LLMs can respond to natural human language and use data analysis to answer unstructured questions or prompts appropriately. A typical computer program would not recognize a prompt like "Who are the four greatest punk bands in history?" but an LLM can provide a list of bands along with reasonable and persuasive logic for why they are the best.

However, LLMs can only provide information as reliable as the data they are trained on. Incorrect data leads to incorrect responses. LLMs may sometimes produce "hallucinations," generating fake information when unable to provide accurate answers. For example, in 2022, the news media Fast Company asked ChatGPT about Tesla's last fiscal quarter. ChatGPT produced a consistent news article, but much of the information was fabricated.

From a security perspective, LLM-based user-facing applications are susceptible to bugs like other applications. Malicious input can manipulate an LLM to prioritize risky or unethical responses over others. Lastly, one security issue with LLMs is that users may upload confidential data to them to boost productivity. However, since LLMs use received inputs to continue learning, confidential data might be exposed in responses to other users' queries.

### How Do LLMs Work?

### Machine Learning and Deep Learning

At a fundamental level, LLMs are based on machine learning, a subset of AI. Machine learning involves feeding a program with vast amounts of data to teach it how to identify features in the data without human intervention.

LLMs use a type of machine learning called deep learning. Deep learning models can recognize distinctions independently, though they typically require some fine-tuning.

Deep learning uses probabilities for "learning." For example, in the sentence "The quick brown fox jumped over the lazy dog," the letters "e" and "o" appear most frequently, each occurring four times. This allows the deep learning model to (correctly) conclude that these letters are most likely to appear in English text.

In practice, a deep learning model cannot draw conclusions from a single sentence. However, after analyzing trillions of sentences, it can learn to predict how to logically complete or generate sentences.

### Neural Networks

To enable this type of deep learning, LLMs are built on neural networks. Just as the human brain consists of neurons that connect and send signals to each other, artificial neural networks (often shortened to "neural networks") consist of network nodes that connect to each other. These networks are composed of multiple "layers": an input layer, an output layer, and one or more layers in between. Layers only pass information to each other if their output exceeds a certain threshold.

### Transformer Models

The specific kind of neural network used in LLMs is called a transformer model. Transformer models can learn context, which is crucial for human language, as context can drastically change meaning. Transformer models use a mathematical technique called self-attention to detect subtle relationships between elements in a sequence. Therefore, transformer models understand context better than other types of machine learning. For example, they can understand how the end and beginning of a sentence are connected, or how sentences in a paragraph relate to each other.

This allows LLMs to interpret human language that is ambiguous, poorly defined, arranged in unfamiliar combinations, or contextualized in new ways. To some extent, LLMs "understand" semantics by grouping words and concepts millions or billions of times according to their meanings.

### How Developers Can Quickly Start Building Their Own LLMs

To build LLM applications, developers need easy access to various datasets and a place to store them. Both cloud storage and on-premises storage for these purposes can require significant infrastructure investment, often outside a developer's budget. Additionally, training datasets are typically stored in multiple locations, and centralizing this data can incur substantial egress fees.

Fortunately, Cloudflare offers several services to help developers quickly start building LLM applications and other types of AI. Vectorize is a globally distributed vector database that can query data stored in egress-free object storage (R2) or documents stored in Workers KV. Combined with Cloudflare's development platform, Workers AI, developers can quickly start experimenting with their LLMs using Cloudflare.