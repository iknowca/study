package com.iknow.study.web.jwdw.springex.sample;

import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Repository;

@Repository
//@Primary
@Qualifier("sampleDAO2")
public class SampleDAO2 implements SampleDAO {
}
