import pathway as pw
from pathway.xpacks.llm import prompts
from pathway.xpacks.llm.tests.utils import create_rag_app


def test_query_transform_callable_and_udf():
    # callable should be wrapped into pw.UDF by the constructor
    def simple_transform(q: str) -> str:
        return q + " transformed"

    rag = create_rag_app(query_transform=simple_transform)

    assert hasattr(rag, "query_transform")
    assert isinstance(rag.query_transform, pw.UDF)

    # passing an existing pw.UDF should be accepted as-is
    rag2 = create_rag_app(query_transform=prompts.prompt_query_rewrite)
    assert hasattr(rag2, "query_transform")
    assert isinstance(rag2.query_transform, pw.UDF)
