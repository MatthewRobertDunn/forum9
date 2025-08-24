const baseUri: string = import.meta.env.VITE_API_BASE_URI;
import type Question from './question';
import type QuestionSummary from './question-summary';
export async function getQuestions(date: Date | null): Promise<QuestionSummary[]> {
    const uri = new URL(`${baseUri}/threads`);
    if (date) {
        uri.searchParams.set('date', date.toISOString());
    }
    console.log(`calling ${uri}`);
    var res = await fetch(uri);
    var json = await res.json();
    return (json as any[]).map(x => ({
        ...x,
        created_date: new Date(x.created_date)
    }))
}

export async function getQuestion(id: string): Promise<Question> {
    const uri = `${baseUri}/threads/${id}`;
    console.log(`calling ${uri}`);
    var res = await fetch(uri);
    var json = await res.json();
    return {
        ...json,
        created_date: new Date(json.created_date)
    }
}


export async function submitQuestion(question: string): Promise<string> {
    const uri = `${baseUri}/threads`;
    console.log(`calling ${uri}`);

    var json = { message: question };
    var res = await fetch(uri, {
        method: 'POST',
        body: JSON.stringify(json),
        headers: {
            'Content-Type': 'application/json'
        }
    });

    var response = await res.json();
    return response;
}