from agents import input_guardrail
from agents import Runner
from agents import GuardrailFunctionOutput
from app_agents import guardrail_agent

# Guardrail function that checks if a user's message contains a personal name, using the guardrail_agent.
@input_guardrail
async def guardrail_against_name(ctx, agent, message):
    result = await Runner.run(guardrail_agent, message, context=ctx.context)
    is_name_in_message = result.final_output.is_name_in_message
    return GuardrailFunctionOutput(output_info={"found_name": result.final_output},tripwire_triggered=is_name_in_message)