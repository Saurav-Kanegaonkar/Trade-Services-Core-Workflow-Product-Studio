# PRD Brief

## Product Bet

Guided reschedule flow for scheduling and dispatch.

## Problem

Dispatchers lose time when urgent calls, skill matching, and arrival windows live in separate mental models. A risky schedule move can create missed windows, customer callbacks, and office follow-up work.

## Hypothesis

A guided reschedule flow with skill, proximity, and customer promise checks will reduce missed windows and support escalations.

## Primary Personas

- Dispatcher: needs a fast way to understand whether a move creates a second problem.
- Service manager: needs exception reasons and coaching signals.
- Customer service rep: needs fewer arrival update calls and cleaner customer communication.

## Requirements

1. Show schedule move risks before confirmation.
2. Require a reason when a move breaks the promised arrival window.
3. Instrument reschedule risk viewed, promise-window exception saved, and reschedule confirmed events.

## Success Metrics

- Reschedule completion rate.
- Missed-window rate.
- Support contact rate for arrival questions.
- Dispatcher time to confirm a schedule move.

## Non-Goals

- No autonomous dispatching in the first release.
- No live route optimization in the first release.
- No replacement of technician capacity planning.
- No pricing, invoicing, or payment logic changes.
