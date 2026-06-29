# Semiconductor AI Assistant

반도체 공정 문서 RAG와 Wafer Map 결함 분류를 통합한 도메인 특화 멀티모달 AI 시스템

## 프로젝트 목표

- 반도체 공정 문서 기반 질의응답 (RAG)
- Wafer Map 결함 패턴 분류 및 분석 (Vision)
- 두 시스템을 통합한 반도체 AI 도우미 완성

## 기술 스택

- **언어**: Python 3.12
- **AI/ML**: PyTorch, timm (Vision Transformer), scikit-learn
- **RAG**: ChromaDB, multilingual-e5-small, Ollama (gemma2:2b)
- **데이터**: WM-811K (811,457장 Wafer Map, CC0)
- **환경**: pyenv, venv, macOS (Apple Silicon / MPS)

## 진행 상황

- [x] 개발 환경 셋업
- [x] Git/GitHub 연동
- [x] Phase 1: RAG 파이프라인 구축
- [x] Phase 2: Wafer Map 결함 분류 (ResNet18 + ViT)
- [ ] 두 시스템 통합

## Phase 1: 반도체 문서 RAG

위키 문서를 청킹 → 임베딩(multilingual-e5-small) → ChromaDB 저장 →
로컬 LLM(Ollama gemma2:2b)으로 질의응답하는 파이프라인.

## Phase 2: Wafer Map 결함 분류

WM-811K 데이터셋의 9가지 결함 패턴(Center, Donut, Edge-Loc, Edge-Ring,
Loc, Near-full, Random, Scratch, none)을 분류하는 비전 모델.

### 주요 과정
- EDA 및 전처리 (라벨 추출, 64×64 리사이즈, stratified split)
- ResNet18 베이스라인 학습
- 클래스 불균형 개선 (class weight 실험)
- CNN vs Transformer 비교 (ResNet18 vs ViT 전이학습)

### 결과 (test set, macro F1 기준)

| 모델 | Accuracy | Macro F1 | 비고 |
|---|---|---|---|
| ResNet18 (baseline) | 0.97 | 0.81 | 가중치 없음 |
| ResNet18 (weighted) | 0.97 | **0.82** | sqrt-softened class weight |
| ViT (pretrained) | 0.97 | 0.78 | 전이학습, train 1/4 사용 |

### 핵심 인사이트
- 클래스 불균형에 단순 `balanced` 가중치 적용 시 과잉보정으로
  macro F1이 오히려 하락(0.81→0.64). 제곱근 완화로 균형점 회복(0.82).
- ViT는 넓게 분포한 패턴(Edge-Ring)에서, CNN은 국소 디테일(Scratch)에서 우월.
- ViT는 학습 데이터 1/4만으로 근접한 성능 → 전이학습의 데이터 효율성 확인.

## 개발자

Yunseongchan (GitHub: josh1261)