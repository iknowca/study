use std::ops::Range;

/// 두 범위가 겹치면 true를 반환한다.
///
///
///    assert_eq!(doc_test::overlap(0..7, 3..10), true);
///    assert_eq!(doc_test::overlap(1..5, 101..105), true);
///
/// 두 범위 중 하나라도 비어있으면 겹치지 않는다고 판단한다.
///
///    assert_eq!(doc_test::overlap(0..0, 0..10), false);
/// 

pub fn overlap(a: Range<usize>, b: Range<usize>) -> bool {
    a.start < a.end && b.start < b.end &&
        a.start < b.end && b.start < a.end
}