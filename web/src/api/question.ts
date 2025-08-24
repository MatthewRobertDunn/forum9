import type { AiResponse } from "./ai-response";
import type QuestionSummary from "./question-summary";
export default interface Question extends QuestionSummary {
    posts: AiResponse[],
    is_processing: boolean | undefined
} 