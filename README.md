# info-extractor

## What is it? 
Personal project that uses OpenAI's API to give summaries on PowerPoint (.ppt, .pptx) and PDF (.pdf) files.

## Why?
Its always a hassle to reread hundreds of PowerPoint slides before exams, so why not use the "power" of AI to summarize.

Its important to be aware that the model I am using is *not perfect*, it will not include EVERY piece of information that
you would want to study before an exam. I would personally use this tool to *suplement* my revisions, not entirely
replace them. 

## How?
Simply pass a relative of full path to a non-empty .pptx, .ppt, or .pdf file when running the program.
<pre>
```shell
python main.py "full_or_relative_path_to_my_file"
```
</pre>

Next, the file path is validated, making sure it exists and is the right file type.

After this has happenend, the file is parsed using tika, and then cleaned up using a regular expression for newlines (parsing PowerPoints leaves massive amounts of newlines ^_^).

Then, we do the AI part. This is split into two parts. 
   Firstly, I authenticate by passing my OpenAI API Key and Org ID into openai (which are hidden from the reader), and then I am ready to go (it really is that simple).

   Secondly, I make a chat completion request. OpenAI makes it very easy to use their models. All of the AI related code is in the 'ai' folder, and most of the LOC in there are error handling. Currently I use the gpt-3.5-turbo-16k model as I realized that I needed to handle a massive amount of tokens.

Once a response has been received from the model, it is error checked. For chat completion requests, we must make sure that the "finish_reason" is nothing other than "stop". More info here: https://platform.openai.com/docs/guides/gpt/chat-completions-api 

Finally, I gave myself two options on how to "consume" the response. 
   Option 1: Simply print out the whole response in the terminal
   Option 2: Save the response as a .txt file in the same directory as the intitial file passed






