# 15 - AI Agents

## Overview

This module introduces **AI Agents** - autonomous systems that combine Large Language Models with tools and reasoning capabilities to complete complex tasks.

## What You'll Learn

- **Agent Fundamentals**: Understanding how AI agents work
- **ReAct Pattern**: Reasoning and Acting in iterative loops
- **Tool Integration**: Giving agents access to external functions and APIs
- **Memory Systems**: Short-term and long-term memory for agents
- **Multi-Step Reasoning**: Breaking down complex tasks
- **Real-World Applications**: Practical use cases and implementations

## Notebooks

### 1. NLP15_1_AI_Agent_Introduction.ipynb
A comprehensive introduction to AI agents with hands-on implementation:
- Building a ReAct agent from scratch
- Implementing multiple tools (calculator, Wikipedia, weather, datetime)
- Adding memory capabilities
- Testing with complex multi-step queries
- Best practices and design patterns

## Key Concepts

### AI Agent Components
1. **LLM Brain**: Decision-making and reasoning
2. **Tools**: Functions the agent can call
3. **Memory**: Context retention across interactions
4. **Planning**: Task decomposition and execution
5. **Reflection**: Self-evaluation and error correction

### Agent Patterns
- **ReAct**: Reasoning + Acting loop
- **Plan-and-Execute**: Planning before execution
- **Reflexion**: Learning from mistakes
- **Multi-Agent**: Specialized agents collaborating

## Tools Implemented

The example agent includes:
- 🧮 **Calculator**: Mathematical computations
- 📚 **Wikipedia Search**: Information retrieval
- 🕒 **DateTime**: Current date and time
- 🌤️ **Weather**: Location-based weather data (mock)

## Prerequisites

```bash
pip install openai python-dotenv requests wikipedia-api
```

Set up your OpenAI API key:
```bash
export OPENAI_API_KEY='your-key-here'
```

## Real-World Applications

- **Customer Support**: Automated helpdesk agents
- **Data Analysis**: Query databases and generate insights
- **Code Assistance**: Development and debugging helpers
- **Research**: Literature review and summarization
- **Task Automation**: Workflow management and scheduling

## Further Learning

### Frameworks
- **LangChain**: Full-featured agent framework
- **LlamaIndex**: Data-focused agents
- **CrewAI**: Multi-agent systems
- **AutoGPT**: Autonomous agent experiments

### Resources
- OpenAI Function Calling Documentation
- ReAct Paper (Yao et al., 2023)
- Reflexion Paper (Shinn et al., 2023)

## Next Steps

After completing this module, you'll be able to:
- ✅ Build custom AI agents for specific tasks
- ✅ Integrate external tools and APIs
- ✅ Design effective agent architectures
- ✅ Deploy agents in production environments

---

**Note**: The agents in this module use OpenAI's GPT models. Ensure you have proper API access and understand usage costs.
