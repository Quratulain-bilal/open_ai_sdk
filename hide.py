import asyncio
from typing import List, Optional

class GuardrailException(Exception):
    pass

# OpenAI-style Base Classes
class BaseInputGuardrail:
    async def __call__(self, input: str) -> None:
        raise NotImplementedError

class BaseOutputGuardrail:
    async def __call__(self, output: str) -> None:
        raise NotImplementedError

# Agent-specific Guardrails (Hidden implementation)
class MathInputGuard(BaseInputGuardrail):
    async def __call__(self, problem: str) -> None:
        if "÷" in problem:  # Hidden check
            raise GuardrailException("Use / instead of ÷")

class MathOutputGuard(BaseOutputGuardrail):
    async def __call__(self, answer: str) -> None:
        if "inf" in answer.lower():
            raise GuardrailException("Infinity results blocked")

class ScienceInputGuard(BaseInputGuardrail):
    async def __call__(self, question: str) -> None:
        if "quantum" in question.lower():
            raise GuardrailException("Complex topics blocked")

class ScienceOutputGuard(BaseOutputGuardrail):
    async def __call__(self, explanation: str) -> None:
        if "42" in explanation:
            raise GuardrailException("Overly simplistic answer")


class MathTeacher:
    def __init__(self):
        
        self.input_guardrails: List[BaseInputGuardrail] = [MathInputGuard()]
        self.output_guardrails: List[BaseOutputGuardrail] = [MathOutputGuard()]

    async def solve(self, problem: str) -> str:
        return f"Result: {eval(problem.replace('^', '**'))}"

class ScienceTeacher:
    def __init__(self):
        
        self.input_guardrails: List[BaseInputGuardrail] = [ScienceInputGuard()]
        self.output_guardrails: List[BaseOutputGuardrail] = [ScienceOutputGuard()]

    async def explain(self, concept: str) -> str:
        return f"Science says: {concept} works through atoms"


class RunConfig:
    def __init__(
        self,
        input_guardrails: Optional[List[BaseInputGuardrail]] = None,
        output_guardrails: Optional[List[BaseOutputGuardrail]] = None
    ):
        self.input_guardrails = input_guardrails or []
        self.output_guardrails = output_guardrails or []


class Runner:
    @classmethod
    async def run(
        cls,
        agent: MathTeacher | ScienceTeacher,
        input: str,
        run_config: RunConfig = None
    ) -> str:
        config = run_config or RunConfig()
        
        
        await cls._execute_guardrails(
            input,
            agent.input_guardrails + config.input_guardrails
        )

        # Agent processing
        result = await (agent.solve(input) if isinstance(agent, MathTeacher) 
                      else agent.explain(input))

        
        await cls._execute_guardrails(
            result,
            agent.output_guardrails + config.output_guardrails
        )

        return result

    @classmethod
    async def _execute_guardrails(
        cls, 
        data: str, 
        guards: List[BaseInputGuardrail | BaseOutputGuardrail]
    ):
        
        await asyncio.gather(*(guard(data) for guard in guards))

# Test
async def main():
    math = MathTeacher()
    science = ScienceTeacher()

    # Math agent with its own guardrails
    try:
        print(await Runner.run(math, "5 ÷ 2"))  # Fails MathInputGuard
    except GuardrailException as e:
        print(f"Math Error: {e}")

    # Science agent with extra run_config guardrail
    try:
        await Runner.run(
            science,
            "life",
            RunConfig(output_guardrails=[ScienceOutputGuard()])  # Extra guardrail
        )
    except GuardrailException as e:
        print(f"Science Error: {e}")

asyncio.run(main())