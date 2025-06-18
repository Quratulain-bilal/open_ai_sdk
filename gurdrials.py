import asyncio
from typing import List, Optional

class GuardrailException(Exception):
    pass

class InputGuardrail:
    async def apply(self, input: str) -> None:
        raise NotImplementedError

class OutputGuardrail:
    async def apply(self, output: str) -> None:
        raise NotImplementedError

# Guardrail Implementations
class MathInputGuard(InputGuardrail):
    async def apply(self, input: str) -> None:
        if "++" in input:
            raise GuardrailException("Invalid math operator")

class MathOutputGuard(OutputGuardrail):
    async def apply(self, output: str) -> None:
        if "∞" in output:
            raise GuardrailException("Infinity not allowed")

class ScienceInputGuard(InputGuardrail):
    async def apply(self, input: str) -> None:
        if "quantum" in input.lower():
            raise GuardrailException("Complex topics not allowed")

class ScienceOutputGuard(OutputGuardrail):
    async def apply(self, output: str) -> None:
        if "42" in output:
            raise GuardrailException("Overly simplistic answer")

# Agents
class MathTeacher:
    def __init__(self):
        self.input_guardrails = [MathInputGuard()]
        self.output_guardrails = [MathOutputGuard()]

    async def solve(self, problem: str) -> str:
        return f"Answer: {eval(problem.replace('^', '**'))}"

class ScienceTeacher:
    def __init__(self):
        self.input_guardrails = [ScienceInputGuard()]
        self.output_guardrails = [ScienceOutputGuard()]

    async def explain(self, concept: str) -> str:
        return f"Explanation: {concept} works through scientific principles"

# Run Configuration
class RunConfig:
    def __init__(
        self,
        input_guardrails: Optional[List[InputGuardrail]] = None,
        output_guardrails: Optional[List[OutputGuardrail]] = None
    ):
        self.input_guardrails = input_guardrails or []
        self.output_guardrails = output_guardrails or []

# Runner 
class Runner:
    @classmethod
    async def run(
        cls,
        agent: MathTeacher | ScienceTeacher,
        input: str,
        run_config: RunConfig = None
    ) -> str:
        config = run_config or RunConfig()
        
        # Combine input guardrails
        input_guards = agent.input_guardrails + config.input_guardrails
        await cls._apply_guards(input, input_guards)

        # Process input
        if isinstance(agent, MathTeacher):
            result = await agent.solve(input)
        else:
            result = await agent.explain(input)

        # Combine output guardrails
        output_guards = agent.output_guardrails + config.output_guardrails
        await cls._apply_guards(result, output_guards)

        return result

    @classmethod
    async def _apply_guards(cls, data: str, guards: List[InputGuardrail | OutputGuardrail]):
        try:
            await asyncio.gather(*(guard.apply(data) for guard in guards))
        except GuardrailException as e:
            raise

# Test Cases
async def main():
    math_teacher = MathTeacher()
    science_teacher = ScienceTeacher()

    # Test 1: Math with valid input
    result = await Runner.run(
        math_teacher,
        "2 + 2",
        RunConfig(input_guardrails=[MathInputGuard()])  
    )
    print(f"Math Test 1: {result}")

    # Test 2: Science with blocked input
    try:
        await Runner.run(
            science_teacher,
            "Explain quantum physics",
            RunConfig(output_guardrails=[ScienceOutputGuard()])
        )
    except GuardrailException as e:
        print(f"Science Test 2: {e}")

    # Test 3: Math with invalid operator
    try:
        await Runner.run(math_teacher, "1 ++ 1")
    except GuardrailException as e:
        print(f"Math Test 3: {e}")

asyncio.run(main())
