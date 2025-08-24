/**
 * Interface representing a summary of a post.
 */
export default interface QuestionSummary {
  id: string;
  question: string;
  created_date: Date;
  count: number;
}