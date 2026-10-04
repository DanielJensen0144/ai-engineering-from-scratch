import Anthropic from "@anthropic-ai/sdk";
import dotenv from 'dotenv';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const envPath = path.resolve(__dirname, '../../../../.env');
dotenv.config({ path: envPath });

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"]
});

const MODEL = process.env.LLM_MODEL ?? "claude-sonnet-5";

console.log(`Using: ${MODEL}`);

const response = await client.messages.create({
  model: MODEL,
  max_tokens: 256,
  messages: [{ role: "user", content: "What is a neural network in one sentence?" }]
});

for (const block of response.content) {
  if (block.type == "text") {
    console.log(block.text);
  }
}
